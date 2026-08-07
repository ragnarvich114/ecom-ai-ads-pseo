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
        return f"""
        <h2>Executive Summary: Why {tool_name} is Dominating {category} in 2026</h2>
        <p>In today's fast-paced e-commerce environment, scaling efficiently requires specialized software. <strong>{tool_name}</strong> delivers exceptional value starting at ${price}/month.</p>
        <div class="my-8"><img src="https://images.unsplash.com/photo-1551288049-bebda4e38f71?auto=format&fit=crop&w=1200&q=80" alt="{tool_name}" class="rounded-2xl shadow-md border border-slate-200 w-full object-cover h-80"></div>
        <h2>Deep-Dive Feature Breakdown</h2>
        <ul><li><strong>Core Feature:</strong> {features[0] if features else 'Advanced automation'}</li></ul>
        <h2>Conclusion</h2>
        <p>An essential tool for modern e-commerce brands looking to scale profitability.</p>
        """

def get_navbar_html():
    return """
    <header class="sticky top-0 z-50 bg-white/95 backdrop-blur-sm border-b border-slate-200 shadow-sm">
        <div class="max-w-7xl mx-auto px-4 h-20 flex items-center justify-between">
            <a href="index.html" class="flex items-center gap-2 font-extrabold text-xl text-slate-900 no-underline">
                <div class="w-9 h-9 bg-indigo-600 text-white rounded-lg flex items-center justify-center">AI</div>
                <span>EcomStack</span>
            </a>
            <nav class="hidden xl:flex items-center gap-4 font-semibold text-xs text-slate-600 uppercase tracking-wide">
                <a href="ai-video-and-content.html" class="hover:text-indigo-600">Video</a>
                <a href="ai-dropshipping.html" class="hover:text-indigo-600">Dropship</a>
                <a href="marketing-and-email.html" class="hover:text-indigo-600">Marketing</a>
                <a href="seo-and-traffic.html" class="hover:text-indigo-600">SEO</a>
                <a href="inventory-and-logistics.html" class="hover:text-indigo-600">Inventory</a>
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
                    <a href="ai-video-and-content.html" class="hover:text-white">AI Video</a>
                    <a href="ai-dropshipping.html" class="hover:text-white">AI Dropshipping</a>
                    <a href="marketing-and-email.html" class="hover:text-white">Marketing</a>
                    <a href="seo-and-traffic.html" class="hover:text-white">SEO</a>
                </div>
            </div>
            <div>
                <h4 class="text-white font-bold mb-4">Operations</h4>
                <div class="flex flex-col gap-2">
                    <a href="inventory-and-logistics.html" class="hover:text-white">Inventory</a>
                    <a href="support.html" class="hover:text-white">Support</a>
                    <a href="shipping.html" class="hover:text-white">Shipping</a>
                </div>
            </div>
            <div>
                <h4 class="text-white font-bold mb-4">Optimization</h4>
                <div class="flex flex-col gap-2">
                    <a href="analytics.html" class="hover:text-white">Analytics</a>
                    <a href="loyalty.html" class="hover:text-white">Loyalty</a>
                    <a href="cro.html" class="hover:text-white">CRO</a>
                </div>
            </div>
        </div>
    </footer>
    """

REVIEW_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>__NAME__ Review (2026): Is It Worth $__PRICE__/mo? | EcomStack</title>
    <script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="bg-slate-50 text-slate-800 antialiased flex flex-col justify-between min-h-screen">
    __NAVBAR__
    <header class="bg-indigo-50 py-16 px-6 border-b border-slate-200">
        <div class="max-w-5xl mx-auto">
            <h1 class="text-4xl font-extrabold text-slate-900 mb-4">__NAME__ Review (2026): Is It Worth $<span class="text-indigo-600">__PRICE__</span>/mo?</h1>
            <p class="text-lg text-slate-600 mb-6">__DESCRIPTION__</p>
            <div class="rounded-3xl overflow-hidden shadow-xl border border-slate-200"><img src="__HERO_IMAGE__" class="w-full h-96 object-cover" alt="__NAME__"></div>
        </div>
    </header>
    <main class="max-w-5xl mx-auto px-6 py-12 grid lg:grid-cols-3 gap-12 w-full">
        <article class="lg:col-span-2 bg-white border border-slate-200 rounded-2xl p-8 shadow-sm space-y-6 text-slate-700 leading-relaxed text-lg">
            __AI_ARTICLE_BODY__
        </article>
        <aside class="space-y-6">
            <div class="sticky top-28 bg-slate-900 text-white rounded-2xl p-8 shadow-xl">
                <h3 class="text-xl font-bold mb-3">Ready to scale __NAME__?</h3>
                <a href="__AFFILIATE_LINK__" target="_blank" rel="noopener" class="block bg-indigo-500 hover:bg-indigo-400 text-white font-bold py-3.5 rounded-xl text-center shadow-lg">Claim Free Trial</a>
            </div>
        </aside>
    </main>
    __FOOTER__
</body>
</html>
"""

INDEX_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>EcomStack | E-commerce Software Directory</title>
    <script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="bg-slate-50 text-slate-800 antialiased flex flex-col justify-between min-h-screen">
    __NAVBAR__
    <section class="bg-indigo-50 py-20 px-6 text-center border-b border-slate-200">
        <div class="max-w-4xl mx-auto">
            <h1 class="text-5xl font-extrabold text-slate-900 mb-6">Scale Your E-commerce Brand With <span class="text-indigo-600">Top Software & AI</span></h1>
            <p class="text-xl text-slate-600">In-depth software reviews, comparisons, and directories for modern DTC founders.</p>
        </div>
    </section>
    <main class="max-w-7xl mx-auto px-6 py-16 w-full flex-grow">
        <h2 class="text-2xl font-bold text-slate-900 mb-8">All Software Reviews</h2>
        <div class="grid md:grid-cols-3 gap-8">__CARDS_HTML__</div>
    </main>
    __FOOTER__
</body>
</html>
"""

def generate_site():
    ensure_output_dir()
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            software_list = json.load(f)
    except FileNotFoundError:
        print(f"[!] {DATA_FILE} not found.")
        return

    hero_images = [
        "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?auto=format&fit=crop&w=1200&q=80",
        "https://images.unsplash.com/photo-1460925895917-afdab827c52f?auto=format&fit=crop&w=1200&q=80",
        "https://images.unsplash.com/photo-1551288049-bebda4e38f71?auto=format&fit=crop&w=1200&q=80"
    ]

    index_cards_html = ""
    for idx, item in enumerate(software_list):
        name = item['name']
        category = item['category']
        price = str(item['starting_price'])
        desc = item.get('description', '')
        aff_link = item.get('affiliate_link', '#')
        slug = name.lower().replace(".", "").replace(" ", "-") + "-review"
        filepath = os.path.join(OUTPUT_DIR, f"{slug}.html")
        hero_img = hero_images[idx % len(hero_images)]

        ai_article_body = generate_human_touch_article(name, category, price, item['features'])

        index_cards_html += f"""
        <a href="{slug}.html" class="bg-white border border-slate-200 rounded-2xl p-8 shadow-sm hover:shadow-xl transition-all flex flex-col justify-between">
            <div>
                <span class="inline-block bg-indigo-50 text-indigo-700 text-xs font-bold uppercase px-3 py-1 rounded-full mb-4">{category}</span>
                <h3 class="text-xl font-bold text-slate-900 mb-2">{name} Review (2026)</h3>
                <p class="text-slate-600 text-sm mb-6">{desc}</p>
            </div>
            <span class="font-semibold text-sm text-indigo-600">Read Review ➔</span>
        </a>
        """

        page_content = (REVIEW_TEMPLATE
                        .replace("__NAVBAR__", get_navbar_html())
                        .replace("__FOOTER__", get_footer_html())
                        .replace("__NAME__", name)
                        .replace("__CATEGORY__", category)
                        .replace("__PRICE__", price)
                        .replace("__DESCRIPTION__", desc)
                        .replace("__AFFILIATE_LINK__", aff_link)
                        .replace("__HERO_IMAGE__", hero_img)
                        .replace("__AI_ARTICLE_BODY__", ai_article_body))

        with open(filepath, "w", encoding="utf-8") as f:
            f.write(page_content)

    index_page = (INDEX_TEMPLATE
                  .replace("__NAVBAR__", get_navbar_html())
                  .replace("__FOOTER__", get_footer_html())
                  .replace("__CARDS_HTML__", index_cards_html))

    with open(os.path.join(OUTPUT_DIR, "index.html"), "w", encoding="utf-8") as f:
        f.write(index_page)

    print("[+] BUILD COMPLETE: All files generated successfully with the new navigation bar.")

if __name__ == "__main__":
    generate_site()