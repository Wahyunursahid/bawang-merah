import streamlit as st

# Menambahkan CSS khusus untuk kontras yang lebih baik
st.markdown(
    """
    <style>
    .main {
        background-color: #ffffff; /* Warna latar belakang putih */
        padding: 20px;
        border-radius: 10px;
    }
    .stButton > button {
        background-color: #4CAF50;
        color: white;
        padding: 10px 24px;
        font-size: 16px;
        border: none;
        border-radius: 5px;
        cursor: pointer;
    }
    .stButton > button:hover {
        background-color: #45a049;
    }
    .header {
        font-size: 36px;
        font-weight: bold;
        color: #333333; /* Warna font gelap */
        text-align: center;
        padding: 20px 0;
    }
    .subheader {
        font-size: 24px;
        color: #555555; /* Warna font lebih gelap */
        text-align: center;
        padding-bottom: 20px;
    }
    .stCheckbox > label {
        font-size: 16px;
        color: #333333; /* Warna font gelap */
    }
    .error-message {
        color: red;
        font-weight: bold;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Menggunakan Bootstrap untuk styling tambahan
st.markdown(
    """
    <link href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" rel="stylesheet">
    """,
    unsafe_allow_html=True
)

class ForwardChainingExpertSystem:
    def __init__(self):
        self.rules = {
            'Akar Busuk': ['Akar hitam', 'Tanaman layu', 'Pertumbuhan lambat'],
            'Daun Kuning': ['Daun menguning', 'Bercak coklat pada daun'],
            'Bercak Daun': ['Bercak hitam pada daun', 'Daun rontok'],
            'Busuk Batang': ['Batang menghitam', 'Batang lembek'],
        }
        self.knowledge_base = []

    def add_symptom(self, symptom):
        if symptom not in self.knowledge_base:
            self.knowledge_base.append(symptom)

    def diagnose(self):
        for disease, symptoms in self.rules.items():
            if all(symptom in self.knowledge_base for symptom in symptoms):
                return disease
        return 'Penyakit tidak terdeteksi'

# Inisialisasi sistem pakar
expert_system = ForwardChainingExpertSystem()

# Gejala yang tersedia
symptoms = [
    'Akar hitam',
    'Tanaman layu',
    'Pertumbuhan lambat',
    'Daun menguning',
    'Bercak coklat pada daun',
    'Bercak hitam pada daun',
    'Daun rontok',
    'Batang menghitam',
    'Batang lembek'
]

# Menampilkan header dan subheader
st.markdown('<div class="header">Sistem Pakar Diagnosa Penyakit Tanaman</div>', unsafe_allow_html=True)
st.markdown('<div class="subheader">Pilih tepat 2 gejala untuk mendapatkan diagnosa</div>', unsafe_allow_html=True)

# Membuat widget checkbox untuk masing-masing gejala
symptom_checkboxes = [st.checkbox(symptom) for symptom in symptoms]

# Tombol untuk submit
submit_button = st.button("Submit")

# Label untuk menampilkan hasil diagnosis
result_label = st.empty()

# Label untuk menampilkan pesan kesalahan
error_label = st.empty()

# Fungsi untuk menangani event klik pada tombol submit
if submit_button:
    selected_symptoms = [symptoms[i] for i in range(len(symptom_checkboxes)) if symptom_checkboxes[i]]
    if len(selected_symptoms) != 2:
        error_label.error("Harap pilih tepat 2 gejala.", icon="🚨")
    else:
        error_label.empty()
        expert_system.knowledge_base = selected_symptoms
        diagnosis = expert_system.diagnose()
        result_label.success(f"Diagnosis penyakit: {diagnosis}")
