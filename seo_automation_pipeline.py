import json
import os

OUTPUT_DIR = "./public"
DATA_FILE = "software_db.json"

def ensure_output_dir():
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

def get_navbar_html():
    return """
    <header class="sticky top-0 z-50 bg-white/90 backdrop-blur-md border-b border-slate-200 shadow-sm">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-20 flex items-center justify-between">
            <a href="index.html" class="flex items-center gap-2.5 font-extrabold text-xl text-slate-900 no-underline">
                <div class="w-9 h-9 bg-indigo-600 text-white rounded-lg flex items-center justify-center font-bold text-lg shadow-md shadow-indigo-200">AI</div>
                <span>EcomStack</span>
            </a>
            <nav class="hidden md:flex items-center gap-8 font-semibold text-sm text-slate-600">
                <a href="ai-video-and-content.html" class="hover:text-indigo-600 transition-colors">AI Video</a>
                <a href="marketing-and-email.html" class="hover:text-indigo-600 transition-colors">Marketing</a>
                <a href="seo-and-traffic.html" class="hover:text-indigo-600 transition-colors">SEO</a>
                <a href="inventory-and-logistics.html" class="hover:text-indigo-600 transition-colors">Inventory</a>
            </nav>
            <a href="index.html" class="bg-indigo-600 hover:bg-indigo-700 text-white font-semibold px-5 py-2.5 rounded-full text-sm shadow-md shadow-indigo-200 transition-colors">Directory Hub</a>
        </div>
    </header>
    """

def get_footer_html():
    return """
    <footer class="bg-slate-900 text-slate-400 py-12 px-6 border-t border-slate-800 text-center text-sm">
        <div class="max-w-7xl mx-auto flex flex-col md:flex-row items-center justify-between gap-4">
            <div>&copy; 2026 EcomStack. All rights reserved. Professional E-commerce Software Directory.</div>
            <div class="flex gap-6 justify-center">
                <a href="index.html" class="hover:text-white transition-colors">Directory Hub</a>
                <a href="ai-video-and-content.html" class="hover:text-white transition-colors">AI Video</a>
                <a href="marketing-and-email.html" class="hover:text-white transition-colors">Marketing</a>
                <a href="seo-and-traffic.html" class="hover:text-white transition-colors">SEO</a>
            </div>
        </div>
    </footer>
    """

REVIEW_TEMPLATE = """<!DOCTYPE html>
<html lang="en" class="scroll-smooth">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>__NAME__ Review (2026): Is It Worth $__PRICE__/mo? | EcomStack</title>
    <meta name="description" content="Read our exhaustive 2026 review of __NAME__. We analyze its AI capabilities, pricing tiers, operational workflows, pros and cons, and ROI for E-commerce brands.">
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
    <style>body { font-family: 'Inter', sans-serif; }</style>
</head>
<body class="bg-slate-50 text-slate-800 antialiased flex flex-col justify-between min-h-screen">

    __NAVBAR__

    <header class="bg-gradient-to-b from-indigo-50/50 to-slate-50 py-16 px-6 border-b border-slate-200">
        <div class="max-w-5xl mx-auto">
            <span class="inline-block bg-indigo-100 text-indigo-800 text-xs font-bold uppercase tracking-wider px-3 py-1 rounded-full mb-4">__CATEGORY__ Review</span>
            <h1 class="text-4xl md:text-5xl font-extrabold text-slate-900 tracking-tight leading-tight mb-6">
                __NAME__ Review (2026): Is It Worth <span class="text-indigo-600">$__PRICE__/mo?</span>
            </h1>
            <p class="text-lg text-slate-600 max-w-3xl leading-relaxed mb-8">__DESCRIPTION__</p>
            <div class="flex gap-4 flex-wrap">
                <a href="#" class="bg-indigo-600 hover:bg-indigo-700 text-white font-bold py-3.5 px-8 rounded-xl shadow-lg shadow-indigo-200 transition-all">Start Free Trial ➔</a>
                <a href="#features" class="bg-white hover:bg-slate-100 text-slate-700 font-semibold py-3.5 px-8 rounded-xl border border-slate-200 transition-all">View Features</a>
            </div>
        </div>
    </header>

    <main class="max-w-5xl mx-auto px-6 py-12 grid lg:grid-cols-3 gap-12 w-full">
        <article class="lg:col-span-2 space-y-8">
            <div class="bg-white border border-slate-200 rounded-2xl p-8 shadow-sm">
                <h2 class="text-2xl font-bold text-slate-900 mb-4">Comprehensive Overview</h2>
                <p class="text-slate-600 leading-relaxed mb-4">In today's highly competitive e-commerce landscape, scaling a store requires leveraging specialized SaaS tools that automate complex workflows. <strong>__NAME__</strong> stands out in the <strong>__CATEGORY__</strong> category by providing robust tooling starting at <strong>$__PRICE__/month</strong>.</p>
                <p class="text-slate-600 leading-relaxed">Whether you are managing multi-channel operations, optimizing ad campaigns, or driving customer retention, __NAME__ offers an integrated feature set designed to maximize return on investment.</p>
            </div>

            <div id="features" class="bg-white border border-slate-200 rounded-2xl p-8 shadow-sm">
                <h2 class="text-2xl font-bold text-slate-900 mb-6">Key Features & Capabilities</h2>
                <div class="grid gap-3">
                    __FEATURES_HTML__
                </div>
            </div>

            <div class="bg-white border border-slate-200 rounded-2xl p-8 shadow-sm">
                <h2 class="text-2xl font-bold text-slate-900 mb-6">Ecosystem Integrations</h2>
                <div class="flex flex-wrap gap-2.5">
                    __INTEGRATIONS_HTML__
                </div>
            </div>
        </article>

        <aside class="space-y-6">
            <div class="sticky top-28 bg-slate-900 text-white rounded-2xl p-8 shadow-xl">
                <div class="text-indigo-400 font-bold uppercase text-xs tracking-wider mb-2">Expert Verdict</div>
                <h3 class="text-xl font-bold mb-3">Ready to scale __NAME__?</h3>
                <p class="text-slate-400 text-sm mb-6 leading-relaxed">Join thousands of DTC merchants optimizing their workflow with __NAME__ today.</p>
                <a href="#" class="block bg-indigo-500 hover:bg-indigo-400 text-white font-bold py-3.5 rounded-xl text-center transition-colors shadow-lg shadow-indigo-900">Claim Free Trial</a>
            </div>
        </aside>
    </main>

    __FOOTER__

</body>
</html>
"""

CATEGORY_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>__CATEGORY_NAME__ Software & Guides | EcomStack</title>
    <meta name="description" content="Explore our expert reviews and guides for __CATEGORY_NAME__ tools, apps, and AI software in 2026.">
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
    <style>body { font-family: 'Inter', sans-serif; }</style>
</head>
<body class="bg-slate-50 text-slate-800 antialiased flex flex-col justify-between min-h-screen">

    __NAVBAR__

    <section class="bg-gradient-to-b from-indigo-50/50 to-slate-50 py-16 px-6 text-center border-b border-slate-200">
        <div class="max-w-4xl mx-auto">
            <span class="inline-block bg-indigo-100 text-indigo-800 text-xs font-bold uppercase tracking-wider px-3 py-1 rounded-full mb-4">Category Hub</span>
            <h1 class="text-4xl md:text-5xl font-extrabold text-slate-900 tracking-tight mb-4">__CATEGORY_NAME__</h1>
            <p class="text-lg text-slate-600 max-w-2xl mx-auto leading-relaxed">Discover in-depth reviews, pricing breakdowns, and expert guides for the top __CATEGORY_NAME__ solutions in e-commerce.</p>
        </div>
    </section>

    <main class="max-w-7xl mx-auto px-6 py-16 w-full flex-grow">
        <div class="grid md:grid-cols-2 lg:grid-cols-3 gap-8">
            __CARDS_HTML__
        </div>
    </main>

    __FOOTER__

</body>
</html>
"""

COMPARISON_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>__TOOL_A__ vs __TOOL_B__ (2026): Which is Best for E-commerce? | EcomStack</title>
    <meta name="description" content="Detailed 2026 comparison between __TOOL_A__ and __TOOL_B__. Compare pricing, features, integrations, and ROI for DTC brands.">
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
    <style>body { font-family: 'Inter', sans-serif; }</style>
</head>
<body class="bg-slate-50 text-slate-800 antialiased flex flex-col justify-between min-h-screen">

    __NAVBAR__

    <header class="bg-gradient-to-b from-indigo-50/50 to-slate-50 py-16 px-6 border-b border-slate-200 text-center">
        <div class="max-w-4xl mx-auto">
            <span class="inline-block bg-indigo-100 text-indigo-800 text-xs font-bold uppercase tracking-wider px-3 py-1 rounded-full mb-4">Software Face-off</span>
            <h1 class="text-4xl md:text-5xl font-extrabold text-slate-900 tracking-tight mb-6">
                __TOOL_A__ vs __TOOL_B__ (2026): Head-to-Head Comparison
            </h1>
            <p class="text-lg text-slate-600 max-w-2xl mx-auto leading-relaxed">We compare pricing, core features, integrations, and ROI to help you choose the right tool for your e-commerce store.</p>
        </div>
    </header>

    <main class="max-w-5xl mx-auto px-6 py-16 w-full space-y-12">
        <div class="grid md:grid-cols-2 gap-8">
            <div class="bg-white border border-slate-200 rounded-2xl p-8 shadow-sm flex flex-col justify-between">
                <div>
                    <span class="inline-block bg-indigo-50 text-indigo-700 text-xs font-bold uppercase tracking-wider px-3 py-1 rounded-full mb-3">Option A</span>
                    <h2 class="text-2xl font-bold text-slate-900 mb-2">__TOOL_A__</h2>
                    <p class="text-indigo-600 font-semibold mb-4">Starting at $__PRICE_A__/mo</p>
                    <p class="text-slate-600 text-sm leading-relaxed mb-6">__DESC_A__</p>
                </div>
                <a href="__SLUG_A__.html" class="block bg-slate-900 hover:bg-slate-800 text-white font-semibold py-3 rounded-xl text-center transition-colors">Read Full __TOOL_A__ Review ➔</a>
            </div>

            <div class="bg-white border border-slate-200 rounded-2xl p-8 shadow-sm flex flex-col justify-between">
                <div>
                    <span class="inline-block bg-indigo-50 text-indigo-700 text-xs font-bold uppercase tracking-wider px-3 py-1 rounded-full mb-3">Option B</span>
                    <h2 class="text-2xl font-bold text-slate-900 mb-2">__TOOL_B__</h2>
                    <p class="text-indigo-600 font-semibold mb-4">Starting at $__PRICE_B__/mo</p>
                    <p class="text-slate-600 text-sm leading-relaxed mb-6">__DESC_B__</p>
                </div>
                <a href="__SLUG_B__.html" class="block bg-slate-900 hover:bg-slate-800 text-white font-semibold py-3 rounded-xl text-center transition-colors">Read Full __TOOL_B__ Review ➔</a>
            </div>
        </div>

        <article class="bg-white border border-slate-200 rounded-2xl p-8 md:p-12 shadow-sm space-y-6 text-slate-700 leading-relaxed text-lg">
            <h2 class="text-2xl font-bold text-slate-900">Which One Should You Choose?</h2>
            <p>When deciding between <strong>__TOOL_A__</strong> and <strong>__TOOL_B__</strong>, your choice ultimately comes down to budget and specific workflow requirements. If you need advanced category-leading features, __TOOL_A__ provides exceptional value starting at $<span id="pa">__PRICE_A__</span>/mo.</p>
            <p>Conversely, if your brand prioritizes specialized integrations and streamlined scaling, __TOOL_B__ is a formidable contender.</p>
        </article>
    </main>

    __FOOTER__

</body>
</html>
"""

INDEX_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>EcomStack | E-commerce Software Directory & Comparisons</title>
    <meta name="description" content="Discover, compare, and review the best e-commerce software, AI video tools, marketing automation, and inventory platforms in 2026.">
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
    <style>body { font-family: 'Inter', sans-serif; }</style>
</head>
<body class="bg-slate-50 text-slate-800 antialiased flex flex-col justify-between min-h-screen">

    __NAVBAR__

    <section class="bg-gradient-to-b from-indigo-50/60 to-slate-50 py-20 px-6 text-center border-b border-slate-200">
        <div class="max-w-4xl mx-auto">
            <span class="inline-block bg-indigo-100 text-indigo-800 text-xs font-bold uppercase tracking-wider px-3.5 py-1.5 rounded-full mb-6 shadow-sm">2026 E-commerce Software Hub</span>
            <h1 class="text-4xl md:text-6xl font-extrabold text-slate-900 tracking-tight leading-tight mb-6">
                Scale Your E-commerce Brand With <span class="text-indigo-600">Top Software & AI</span>
            </h1>
            <p class="text-xl text-slate-600 max-w-2xl mx-auto leading-relaxed mb-10">In-depth software reviews, head-to-head comparisons, and strategic guides for modern DTC founders.</p>
            <div class="flex justify-center gap-4 flex-wrap">
                <a href="ai-video-and-content.html" class="bg-indigo-600 hover:bg-indigo-700 text-white font-bold py-3.5 px-8 rounded-xl shadow-lg shadow-indigo-200 transition-all">Explore AI Video Tools ➔</a>
                <a href="#comparisons" class="bg-white hover:bg-slate-100 text-slate-700 font-semibold py-3.5 px-8 rounded-xl border border-slate-200 transition-all">View Comparisons</a>
            </div>
        </div>
    </section>

    <!-- AI Video Editorial Banner -->
    <section class="max-w-7xl mx-auto px-6 pt-16 w-full">
        <div class="bg-slate-900 text-white rounded-3xl p-8 md:p-12 shadow-2xl flex flex-col md:flex-row items-center justify-between gap-8">
            <div class="max-w-2xl">
                <span class="inline-block bg-indigo-500/30 text-indigo-300 border border-indigo-500/40 text-xs font-bold uppercase tracking-wider px-3 py-1 rounded-full mb-4">Featured Editorial Guide</span>
                <h2 class="text-3xl md:text-4xl font-extrabold tracking-tight mb-4">Why AI Video is Transforming E-commerce in 2026</h2>
                <p class="text-slate-300 leading-relaxed mb-6">From cinematic product demonstrations using Higgsfield to automated ad generation with OpenArt and AdCreative, discover how modern DTC brands use generative video to slash customer acquisition costs.</p>
                <a href="importance-of-ai-video-in-ecommerce.html" class="inline-block bg-indigo-600 hover:bg-indigo-500 text-white font-bold py-3 px-6 rounded-xl transition-colors">Read Full Guide ➔</a>
            </div>
            <div class="w-full md:w-auto bg-slate-800/80 border border-slate-700 rounded-2xl p-6 text-center shrink-0">
                <div class="text-3xl font-extrabold text-indigo-400 mb-1">3.4x</div>
                <div class="text-sm text-slate-400">Higher ROAS with AI Video Ads</div>
            </div>
        </div>
    </section>

    <!-- COMPARISON SECTION -->
    <section id="comparisons" class="max-w-7xl mx-auto px-6 py-16 w-full">
        <h2 class="text-2xl font-bold text-slate-900 mb-8">Head-to-Head Software Comparisons</h2>
        <div class="grid md:grid-cols-2 lg:grid-cols-3 gap-8">
            __COMPARISON_CARDS__
        </div>
    </section>

    <main class="max-w-7xl mx-auto px-6 pb-16 w-full">
        <h2 class="text-2xl font-bold text-slate-900 mb-8">All Software Reviews & Articles</h2>
        <div class="grid md:grid-cols-2 lg:grid-cols-3 gap-8">
            __CARDS_HTML__
        </div>
    </main>

    __FOOTER__

</body>
</html>
"""

AI_VIDEO_GUIDE_TEMPLATE = """<!DOCTYPE html>
<html lang="en" class="scroll-smooth">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Why AI Video is Transforming E-commerce in 2026 | EcomStack</title>
    <meta name="description" content="Discover how AI video generation tools like Higgsfield and OpenArt are revolutionizing digital advertising and storytelling for e-commerce brands.">
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
    <style>body { font-family: 'Inter', sans-serif; }</style>
</head>
<body class="bg-slate-50 text-slate-800 antialiased flex flex-col justify-between min-h-screen">

    __NAVBAR__

    <header class="bg-gradient-to-b from-indigo-50/50 to-slate-50 py-16 px-6 border-b border-slate-200">
        <div class="max-w-4xl mx-auto text-center">
            <span class="inline-block bg-indigo-100 text-indigo-800 text-xs font-bold uppercase tracking-wider px-3 py-1 rounded-full mb-4">Strategic Editorial</span>
            <h1 class="text-4xl md:text-5xl font-extrabold text-slate-900 tracking-tight leading-tight mb-6">
                Why AI Video is Transforming E-commerce in 2026
            </h1>
            <p class="text-lg text-slate-600 max-w-2xl mx-auto leading-relaxed">How generative video platforms like Higgsfield and OpenArt are replacing traditional video agencies and driving record conversions on TikTok and Meta.</p>
        </div>
    </header>

    <main class="max-w-4xl mx-auto px-6 py-12 space-y-8 w-full">
        <article class="bg-white border border-slate-200 rounded-2xl p-8 md:p-12 shadow-sm space-y-6 text-slate-700 leading-relaxed text-lg">
            <h2 class="text-2xl font-bold text-slate-900">The Death of Traditional Video Production</h2>
            <p>For years, creating high-converting video advertisements required hiring modeling agencies, renting studios, and waiting weeks for post-production. Today, direct-to-consumer (DTC) brands are bypassing these bottlenecks entirely using generative AI video platforms.</p>
            
            <h2 class="text-2xl font-bold text-slate-900">The Power of Tools Like Higgsfield and OpenArt</h2>
            <p>Platforms such as <strong>Higgsfield AI</strong> allow founders to generate cinematic, character-consistent video clips directly from text prompts. Meanwhile, tools like <strong>OpenArt</strong> and <strong>AdCreative.ai</strong> specialize in instant product styling and conversion-optimized ad variations.</p>
            
            <h2 class="text-2xl font-bold text-slate-900">Key Benefits for Online Store Owners</h2>
            <ul class="list-disc pl-6 space-y-3 text-base">
                <li><strong>Radically Lower Costs:</strong> Produce 50+ ad variants for the price of a single traditional studio shoot.</li>
                <li><strong>Unmatched Speed:</strong> Test new creative angles and hooks on TikTok and Meta within hours instead of weeks.</li>
                <li><strong>Dynamic Localization:</strong> Instantly adapt video backgrounds, languages, and models to target global markets.</li>
            </ul>

            <h2 class="text-2xl font-bold text-slate-900">Explore Our Top-Rated AI Video Tools</h2>
            <p>Ready to store's video marketing stack? Explore our in-depth reviews of leading software in our <a href="ai-video-and-content.html" class="text-indigo-600 font-semibold hover:underline">AI Video & Content Hub</a>.</p>
        </article>
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

    # 1. Generate Individual Review Pages
    for item in software_list:
        name = item['name']
        category = item['category']
        price = str(item['starting_price'])
        desc = item.get('description', 'In-depth software review for scaling e-commerce brands.')
        slug = name.lower().replace(".", "").replace(" ", "-") + "-review"
        filepath = os.path.join(OUTPUT_DIR, f"{slug}.html")

        features_html = "".join([f"""
            <div class="flex items-center gap-3 bg-slate-50 border border-slate-100 p-3.5 rounded-xl font-medium text-slate-700">
                <span class="w-6 h-6 rounded-full bg-indigo-50 text-indigo-600 flex items-center justify-center font-bold text-xs shrink-0">✓</span>
                <span>{f}</span>
            </div>
        """ for f in item['features']])

        integrations_html = "".join([f"""
            <span class="bg-white border border-slate-200 text-slate-800 font-semibold px-4 py-2 rounded-xl text-sm shadow-sm">
                {integ}
            </span>
        """ for integ in item['integrations']])

        page_content = (REVIEW_TEMPLATE
                        .replace("__NAVBAR__", get_navbar_html())
                        .replace("__FOOTER__", get_footer_html())
                        .replace("__NAME__", name)
                        .replace("__CATEGORY__", category)
                        .replace("__PRICE__", price)
                        .replace("__DESCRIPTION__", desc)
                        .replace("__FEATURES_HTML__", features_html)
                        .replace("__INTEGRATIONS_HTML__", integrations_html))

        with open(filepath, "w", encoding="utf-8") as f:
            f.write(page_content)

    # 2. Generate Comparison Pages (e.g., Klaviyo vs Postscript, Surfer vs Semrush, Higgsfield vs OpenArt)
    comparisons = [
        ("Higgsfield AI", "OpenArt AI"),
        ("Klaviyo", "Postscript"),
        ("Surfer SEO", "Semrush Ecom SEO")
    ]

    comparison_cards_html = ""
    for tool_a, tool_b in comparisons:
        item_a = next((x for x in software_list if x['name'] == tool_a), None)
        item_b = next((x for x in software_list if x['name'] == tool_b), None)
        if not item_a or not item_b:
            continue

        slug_a = item_a['name'].lower().replace(".", "").replace(" ", "-") + "-review"
        slug_b = item_b['name'].lower().replace(".", "").replace(" ", "-") + "-review"
        comp_slug = f"{item_a['name'].lower().replace('.', '').replace(' ', '-')}-vs-{item_b['name'].lower().replace('.', '').replace(' ', '-')}.html"
        comp_filepath = os.path.join(OUTPUT_DIR, comp_slug)

        comparison_cards_html += f"""
        <a href="{comp_slug}" class="bg-white border border-slate-200 rounded-2xl p-8 shadow-sm hover:shadow-xl hover:border-indigo-600 transition-all flex flex-col justify-between group">
            <div>
                <span class="inline-block bg-indigo-50 text-indigo-700 text-xs font-bold uppercase tracking-wider px-3 py-1 rounded-full mb-4">Software Face-off</span>
                <h3 class="text-xl font-bold text-slate-900 group-hover:text-indigo-600 transition-colors mb-2">{item_a['name']} vs {item_b['name']} (2026)</h3>
                <p class="text-slate-600 text-sm leading-relaxed mb-6">Compare pricing, features, and integrations to find the right tool for your store.</p>
            </div>
            <div class="flex items-center justify-between border-t border-slate-100 pt-4 font-semibold text-sm text-indigo-600">
                <span>View Comparison</span>
                <span>➔</span>
            </div>
        </a>
        """

        comp_content = (COMPARISON_TEMPLATE
                        .replace("__NAVBAR__", get_navbar_html())
                        .replace("__FOOTER__", get_footer_html())
                        .replace("__TOOL_A__", item_a['name'])
                        .replace("__TOOL_B__", item_b['name'])
                        .replace("__PRICE_A__", str(item_a['starting_price']))
                        .replace("__PRICE_B__", str(item_b['starting_price']))
                        .replace("__DESC_A__", item_a['description'])
                        .replace("__DESC_B__", item_b['description'])
                        .replace("__SLUG_A__", slug_a.replace(".html", ""))
                        .replace("__SLUG_B__", slug_b.replace(".html", "")))

        with open(comp_filepath, "w", encoding="utf-8") as f:
            f.write(comp_content)

    # 3. Group by Category & Generate Category Archive Pages
    categories = {}
    for item in software_list:
        cat = item['category']
        categories.setdefault(cat, []).append(item)

    for cat_name, items in categories.items():
        cat_slug = cat_name.lower().replace(" & ", "-and-").replace(" ", "-") + ".html"
        cat_filepath = os.path.join(OUTPUT_DIR, cat_slug)

        cards_html = ""
        for item in items:
            slug = item['name'].lower().replace(".", "").replace(" ", "-") + "-review"
            cards_html += f"""
            <a href="{slug}.html" class="bg-white border border-slate-200 rounded-2xl p-8 shadow-sm hover:shadow-xl hover:border-indigo-600 transition-all flex flex-col justify-between group">
                <div>
                    <span class="inline-block bg-indigo-50 text-indigo-700 text-xs font-bold uppercase tracking-wider px-3 py-1 rounded-full mb-4">{item['category']}</span>
                    <h3 class="text-xl font-bold text-slate-900 group-hover:text-indigo-600 transition-colors mb-2">{item['name']} Review (2026)</h3>
                    <p class="text-slate-600 text-sm leading-relaxed mb-6">{item.get('description', '')}</p>
                </div>
                <div class="flex items-center justify-between border-t border-slate-100 pt-4 font-semibold text-sm text-indigo-600">
                    <span>Read In-Depth Review</span>
                    <span>➔</span>
                </div>
            </a>
            """

        cat_page = (CATEGORY_TEMPLATE
                    .replace("__NAVBAR__", get_navbar_html())
                    .replace("__FOOTER__", get_footer_html())
                    .replace("__CATEGORY_NAME__", cat_name)
                    .replace("__CARDS_HTML__", cards_html))

        with open(cat_filepath, "w", encoding="utf-8") as f:
            f.write(cat_page)

    # 4. Generate Index Homepage Hub
    index_cards_html = ""
    for item in software_list:
        slug = item['name'].lower().replace(".", "").replace(" ", "-") + "-review"
        index_cards_html += f"""
        <a href="{slug}.html" class="bg-white border border-slate-200 rounded-2xl p-8 shadow-sm hover:shadow-xl hover:border-indigo-600 transition-all flex flex-col justify-between group">
            <div>
                <span class="inline-block bg-indigo-50 text-indigo-700 text-xs font-bold uppercase tracking-wider px-3 py-1 rounded-full mb-4">{item['category']}</span>
                <h3 class="text-xl font-bold text-slate-900 group-hover:text-indigo-600 transition-colors mb-2">{item['name']} Review (2026)</h3>
                <p class="text-slate-600 text-sm leading-relaxed mb-6">{item.get('description', '')}</p>
            </div>
            <div class="flex items-center justify-between border-t border-slate-100 pt-4 font-semibold text-sm text-indigo-600">
                <span>Read In-Depth Review</span>
                <span>➔</span>
            </div>
        </a>
        """

    index_page = (INDEX_TEMPLATE
                  .replace("__NAVBAR__", get_navbar_html())
                  .replace("__FOOTER__", get_footer_html())
                  .replace("__COMPARISON_CAR_CARDS__", comparison_cards_html)
                  .replace("__COMPARISON_CARDS__", comparison_cards_html)
                  .replace("__CARDS_HTML__", index_cards_html))

    with open(os.path.join(OUTPUT_DIR, "index.html"), "w", encoding="utf-8") as f:
        f.write(index_page)

    # 5. Generate Strategic Editorial Guide: AI Video in E-commerce
    guide_path = os.path.join(OUTPUT_DIR, "importance-of-ai-video-in-ecommerce.html")
    guide_page = (AI_VIDEO_GUIDE_TEMPLATE
                  .replace("__NAVBAR__", get_navbar_html())
                  .replace("__FOOTER__", get_footer_html()))
    with open(guide_path, "w", encoding="utf-8") as f:
        f.write(guide_page)

    print("[+] BUILD COMPLETE! All category hubs, comparison face-offs, and review pages compiled successfully.")

if __name__ == "__main__":
    generate_site()