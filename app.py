from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

def get_advice(query):
    query = query.lower()

    # Hindi/Marathi mapping
    if "lal" in query or "red ho gaya" in query:
        query += " red"
    if "peela" in query or "pivla" in query:
        query += " yellow"

    # 🍅 Tomato
    if "tomato" in query:
        if "red" in query:
            return {
                "crop": "टोमॅटो",
                "issue": "फळ लाल होत आहे",
                "solution": "हे नैसर्गिक पिकण्याची प्रक्रिया आहे, कोणतीही समस्या नाही.",
                "tip": "योग्य वेळी काढणी करा आणि जास्त पिकू देऊ नका."
            }
        if "yellow" in query:
            return {
                "crop": "टोमॅटो",
                "issue": "पानं पिवळी होत आहेत",
                "solution": "मातीमध्ये नायट्रोजनची कमतरता असू शकते.",
                "tip": "नायट्रोजन खत वापरा आणि नियमित पाणी द्या."
            }

    # 🌾 Rice
    if "rice" in query or "paddy" in query:
        return {
            "crop": "तांदूळ",
            "issue": "किडीचा प्रादुर्भाव",
            "solution": "नीम तेल किंवा सौम्य कीटकनाशक फवारणी करा.",
            "tip": "दररोज पिकाची तपासणी करा."
        }

    # 🌿 Wheat
    if "wheat" in query:
        return {
            "crop": "गहू",
            "issue": "बुरशीजन्य रोग",
            "solution": "तत्काळ बुरशीनाशक फवारणी करा.",
            "tip": "जास्त पाणी देणे टाळा."
        }

    # Default
    return {
        "crop": "सामान्य",
        "issue": query,
        "solution": "योग्य पाणी आणि सेंद्रिय खतांचा वापर करा.",
        "tip": "समस्या कायम राहिल्यास कृषी तज्ञांचा सल्ला घ्या."
    }

# 🌐 Home route
@app.route("/")
def home():
    return render_template("index.html")

# 🎤 API route
@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json()
    query = data.get("query")

    result = get_advice(query)
    return jsonify(result)

# 🚀 IMPORTANT (missing in your code)
if __name__ == "__main__":
    print("Server starting...")
    app.run(debug=True)