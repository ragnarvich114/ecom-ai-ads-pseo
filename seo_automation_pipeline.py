import json
import os
import google.generativeai as genai

# Configure your Gemini API key 
genai.configure(api_key=os.environ.get("GEMINI_API_KEY", "YOUR_API_KEY"))

OUTPUT_DIR = "./public"
DATA_FILE = "software_db.json"

def ensure_output_dir():
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

def generate_human_touch_article(tool_name, category, price, features):
    model = genai.GenerativeModel("gemini-2.5-flash")
    
    prompt = f"""
    Write an exhaustive, authoritative 2026 e-commerce review for "{tool_name}" ({category}). 
    Price: ${price}/mo. Features: {", ".join(features)}.
    Length: 1,200 words. Use HTML tags (h2, h3, p, ul, li).
    Include <img> tags from Unsplash for visual breaks.
    Structure: Executive Summary, Deep-Dive Features, ROI Analysis, Pros/Cons, FAQ, Verdict.
    Return ONLY clean HTML body content.
    """
    
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"<p>Review for {tool_name} coming soon...</p>"

def get_navbar_html():
    return """
    <header class="sticky top-0 z-50 bg-white/95 backdrop-blur-sm border-b border-slate-200 shadow-sm">
        <div class="max-w-7xl mx-auto px-4 h-20 flex items-center justify-between">
            <a href="index.html" class="flex items-center gap-2 font-extrabold text-xl text-slate-900">
                <div class="w-9 h-9 bg-indigo-600 text-white rounded-lg flex items-center justify-center">AI</div>
                <span>EcomStack</span>
            </a>
            <nav class="hidden xl:flex items-center gap-4 font-semibold text-xs text-slate-600 uppercase tracking-wide">
                <a href="ai-video.html" class="hover:text-indigo-600">Video</a>
                <a href="ai-dropshipping.html" class="hover:text-indigo-600">Dropship</a>
                <a href="marketing.html" class="hover:text-indigo-600">Marketing</a>
                <a href="seo.html" class="hover:text-indigo-600">SEO</a>
                <a href="inventory.html" class="hover:text-indigo-600">Inventory</a>
                <a href="support.html" class="hover:text-indigo-600">Support</a>
                <a href="analytics.html" class="hover:text-indigo-600">Analytics</a>
                <a href="loyalty.html" class="hover:text-indigo-600">Loyalty</a>
                <a href="cro.html" class="hover:text-indigo-600">CRO</a>
                <a href="shipping.html" class="hover:text-indigo-600">Shipping</a>
            </nav>
            <a href="index.html" class="bg-slate-900 hover:bg-slate-800 text-white font-semibold px-5 py-2.5 rounded-full text-sm transition-colors">Directory</a>
        </div>
    </header>
    """

def get_footer_html():
    return """
    <footer class="bg-slate-900 text-slate-400 py-12 px-6 border-t border-slate-800 text-sm">
        <div class="max-w-7xl mx-auto grid grid-cols-2 md:grid-cols-4 gap-8">
            <div class="col-span-2 md:col-span-1">
                <h3 class="text-white font-bold mb-4">EcomStack 2026</h3>
                <p>The definitive AI-powered software directory for modern e-commerce founders.</p>
            </div>
            <div>
                <h4 class="text-white font-bold mb-4">Core Categories</h4>
                <div class="flex flex-col gap-2">
                    <a href="ai-video.html">AI Video</a>
                    <a href="ai-dropshipping.html">AI Dropshipping</a>
                    <a href="marketing.html">Marketing</a>
                    <a href="seo.html">SEO</a>
                </div>
            </div>
            <div>
                <h4 class="text-white font-bold mb-4">Operations</h4>
                <div class="flex flex-col gap-2">
                    <a href="inventory.html">Inventory</a>
                    <a href="support.html">Support</a>
                    <a href="shipping.html">Shipping</a>
                </div>
            </div>
            <div>
                <h4 class="text-white font-bold mb-4">Optimization</h4>
                <div class="flex flex-col gap-2">
                    <a href="analytics.html">Analytics</a>
                    <a href="loyalty.html">Loyalty</a>
                    <a href="cro.html">CRO</a>
                </div>
            </div>
        </div>
    </footer>
    """

# ... [Keep the REST of the generation logic (Templates, generate_site function) the same as before] ...

def generate_site():
    ensure_output_dir()
    # Logic remains the same: load software_db.json, loop items, generate HTML files
    # ...
    print("[+] BUILD COMPLETE: Navigation bar fully updated with all categories.")

if __name__ == "__main__":
    generate_site()