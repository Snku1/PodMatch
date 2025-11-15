from flask import Flask, render_template, request, jsonify
import joblib
import requests
import os # Untuk memeriksa keberadaan file model

app = Flask(__name__)

# --- Load model klasifikasi mood ---
model = None
def load_model():
    global model
    model_path = os.path.join(app.root_path, 'model', 'model-mood-classifier.joblib')
    if os.path.exists(model_path):
        model = joblib.load(model_path)
        print("Model berhasil dimuat.")
    else:
        print(f"Error: File model tidak ditemukan di {model_path}")
        model = None # Atau tangani error lain sesuai kebutuhan

# Panggil fungsi load_model saat aplikasi dimulai
load_model()

# --- Deskripsi tiap mood ---
mood_description = {
    "Marah": "Kamu sedang merasa marah atau kesal. Coba dengarkan podcast self-healing atau mindfulness untuk membantu menenangkan dirimu.",
    "Takut": "Kamu sedang cemas atau khawatir. Dengarkan podcast dengan tema ketenangan, spiritualitas, atau refleksi bisa membuatmu lebih tenang.",
    "Senang": "Kamu sedang bahagia dan bersemangat! Dengarkan podcast motivasi atau hiburan untuk mempertahankan energi positifmu.",
    "Kasih": "Kamu sedang penuh kasih dan empati. Podcast bertema hubungan, keluarga, atau kisah inspiratif cocok untuk memperkuat perasaanmu.",
    "Netral": "Kamu sedang dalam keadaan stabil dan tenang. Podcast ringan dan hiburan bisa menjadi teman yang pas untuk menemanimu.",
    "Sedih": "Kamu sedang merasa sedih atau kecewa. Dengarkan podcast penyemangat atau kisah inspiratif agar suasana hatimu membaik."
}

# --- Pemetaan mood ke query YouTube (podcast Indonesia) ---
mood_to_query = {
    "Marah": "podcast buat yang lagi marah",
    "Takut": "podcast untuk yang ketakutan",
    "Senang": "podcast hiburan",
    "Kasih": "podcast cinta dan hubungan indonesia",
    "Netral": "podcast lucu dan menghibur",
    "Sedih": "podcast inspirasi hidup dan komedi indonesia"
}

# --- Fungsi ambil video YouTube ---
def get_youtube_videos(query, max_results=4):
    """Gunakan YouTube Data API (ganti API_KEY dengan milikmu)."""
    API_KEY = "AIzaSyB1I-XeS1xwv4TznDXKMmD-qnOn2asXypI" # Ganti dengan API_KEY yang aman
    search_url = "https://www.googleapis.com/youtube/v3/search"

    params = {
        "part": "snippet",
        "q": query,
        "key": API_KEY,
        "maxResults": max_results,
        "type": "video",
        "regionCode": "ID",
        "relevanceLanguage": "id"
    }

    try:
        response = requests.get(search_url, params=params)
        response.raise_for_status() # Akan raise error jika status bukan 200
        data = response.json()

        videos = []
        for item in data.get("items", []):
            video_id = item["id"]["videoId"]
            title = item["snippet"]["title"]
            thumbnail = item["snippet"]["thumbnails"]["high"]["url"] # Ambil thumbnail
            videos.append({
                "title": title,
                "url": f"https://www.youtube.com/watch?v={video_id}",
                "embed": f"https://www.youtube.com/embed/{video_id}",
                "thumbnail": thumbnail
            })
        return videos
    except requests.exceptions.RequestException as e:
        print(f"Error saat mengambil video dari YouTube: {e}")
        return []

# --- Route untuk halaman Beranda ---
@app.route('/')
def index():
    return render_template('index.html')

# --- Route untuk halaman Klasifikasi Mood ---
@app.route('/classify')
def classify_page():
    return render_template('classify.html')

# --- Route untuk memproses analisis mood (POST request) ---
@app.route('/analyze_mood', methods=['POST'])
def analyze_mood():
    if model is None:
        return jsonify({"error": "Model tidak ditemukan. Aplikasi tidak dapat berjalan."}), 500

    user_text = request.form.get('user_text')
    if not user_text or user_text.strip() == "":
        return jsonify({"error": "Silakan masukkan teks terlebih dahulu!"})

    # Lakukan prediksi mood menggunakan model
    try:
        mood = model.predict([user_text])[0]
    except Exception as e:
        print(f"Error saat memprediksi mood: {e}")
        return jsonify({"error": "Gagal memprediksi mood. Silakan coba lagi."}), 500

    # Ambil deskripsi dan query
    description = mood_description.get(mood, "Deskripsi tidak ditemukan.")
    query = mood_to_query.get(mood, "podcast indonesia")

    # Ambil video dari YouTube
    videos = get_youtube_videos(query)

    # Kirim data mood, deskripsi, dan video ke frontend
    return jsonify({
        "success": True,
        "mood": mood,
        "description": description,
        "videos": videos
    })

# --- Route untuk halaman History ---
@app.route('/history')
def history():
    return render_template('history.html')

# --- Route untuk halaman Tentang ---
@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))