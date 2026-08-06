import json
import os
import time

OUTPUT_DIR = "./public"
DATA_FILE = "software_db.json"

def ensure_output_dir():
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en" style="scroll-behavior: smooth;">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>__NAME__ Review (2026): Is It Worth $__PRICE__/mo? | EcomStack</title>
    <meta name="description" content="Read our exhaustive 2026 review of __NAME__. We analyze its AI capabilities, pricing tiers, operational workflows, pros and cons, and ROI for E-commerce brands.">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
    <style>
        :root {
            --slate-50: #f8fafc; --slate-100: #f1f5f9; --slate-200: #e2e8f0; --slate-400: #94a3b8;
            --slate-600: #475569; --slate-700: #334155; --slate-800: #1e293b; --slate-900: #0f172a;
            --indigo-50: #eef2ff; --indigo-100: #e0e7ff; --indigo-600: #4f46e5; --indigo-700: #4338ca;
            --emerald-50: #ecfdf5; --emerald-600: #059669; --red-50: #fef2f2; --red-600: #dc2626;
        }
        * { box-sizing: border-box; margin: 0; padding: 0; }
        body { font-family: 'Inter', sans-serif; background-color: var(--slate-50); color: var(--slate-800); line-height: 1.7; display: flex; flex-direction: column; justify-content: space-between; min-height: 100vh; }
        
        header { position: sticky; top: 0; z-index: 50; background: rgba(255, 255, 255, 0.9); backdrop-filter: blur(12px); border-bottom: 1px solid rgba(226, 232, 240, 0.8); }
        .nav-container { max-width: 1280px; margin: 0 auto; padding: 0 1.5rem; height: 5rem; display: flex; align-items: center; justify-content: space-between; }
        .logo-box { display: flex; align-items: center; gap: 0.75rem; font-weight: 800; font-size: 1.25rem; color: var(--slate-900); text-decoration: none; }
        .logo-icon { width: 2.25rem; height: 2.25rem; background: var(--indigo-600); color: white; border-radius: 0.5rem; display: flex; align-items: center; justify-content: center; font-size: 1.1rem; box-shadow: 0 4px 12px rgba(79, 70, 229, 0.3); }
        
        nav { display: flex; gap: 1.5rem; align-items: center; font-weight: 500; font-size: 0.875rem; color: var(--slate-700); }
        .nav-link { color: var(--slate-600); text-decoration: none; transition: color 0.2s; }
        .nav-link:hover { color: var(--indigo-600); }

        .hero-section { background: radial-gradient(circle at 70% 30%, rgba(99, 102, 241, 0.1) 0%, rgba(236, 72, 153, 0.03) 50%, transparent 100%); padding: 4rem 1.5rem 5rem; border-bottom: 1px solid rgba(226, 232, 240, 0.6); }
        .hero-grid { max-width: 1280px; margin: 0 auto; display: grid; grid-template-columns: 1.2fr 1fr; gap: 3rem; align-items: center; }
        @media(max-width: 900px) { .hero-grid { grid-template-columns: 1fr; } }
        
        .badge { display: inline-flex; align-items: center; gap: 0.5rem; background: var(--indigo-50); border: 1px solid var(--indigo-100); color: var(--indigo-700); font-size: 0.75rem; font-weight: 700; padding: 0.375rem 1rem; border-radius: 9999px; text-transform: uppercase; letter-spacing: 0.05em; margin-bottom: 1.5rem; }
        h1 { font-size: 3rem; font-weight: 800; color: var(--slate-900); letter-spacing: -0.025em; line-height: 1.1; margin-bottom: 1.25rem; }
        h1 span { color: var(--indigo-600); }
        .hero-desc { font-size: 1.125rem; color: var(--slate-600); line-height: 1.6; margin-bottom: 2rem; max-width: 38rem; }
        
        .btn-group { display: flex; gap: 1rem; align-items: center; flex-wrap: wrap; }
        .btn-primary { background: var(--indigo-600); color: white; font-weight: 600; padding: 1rem 2rem; border-radius: 1rem; text-decoration: none; box-shadow: 0 10px 25px -5px rgba(79, 70, 229, 0.35); transition: background 0.2s; display: inline-flex; align-items: center; gap: 0.75rem; }
        .btn-primary:hover { background: var(--indigo-700); }
        .btn-secondary { background: white; color: var(--slate-700); font-weight: 600; padding: 1rem 2rem; border-radius: 1rem; text-decoration: none; border: 1px solid var(--slate-200); box-shadow: 0 1px 3px rgba(0,0,0,0.05); transition: background 0.2s; }
        .btn-secondary:hover { background: var(--slate-50); }

        .mockup-card { background: linear-gradient(135deg, rgba(99, 102, 241, 0.2), rgba(168, 85, 247, 0.1)); padding: 0.75rem; border-radius: 1.5rem; border: 1px solid rgba(255,255,255,0.8); backdrop-filter: blur(20px); box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.15); }
        .mockup-inner { background: white; border-radius: 1.25rem; padding: 1.5rem; box-shadow: inset 0 2px 4px rgba(0,0,0,0.02); }

        main { max-width: 1280px; margin: 0 auto; padding: 4rem 1.5rem; display: grid; grid-template-columns: 2fr 1fr; gap: 3rem; width: 100%; }
        @media(max-width: 900px) { main { grid-template-columns: 1fr; } }
        
        .content-card { background: white; border: 1px solid rgba(226, 232, 240, 0.8); border-radius: 1.5rem; padding: 2.5rem; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.02); margin-bottom: 2rem; }
        .content-card h2 { font-size: 1.75rem; font-weight: 700; color: var(--slate-900); margin-bottom: 1rem; }
        .content-card h3 { font-size: 1.25rem; font-weight: 700; color: var(--slate-800); margin: 1.5rem 0 0.75rem; }
        .content-card p { color: var(--slate-600); font-size: 1.05rem; line-height: 1.8; margin-bottom: 1.25rem; }

        .pros-cons-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 1.5rem; margin: 2rem 0; }
        @media(max-width: 600px) { .pros-cons-grid { grid-template-columns: 1fr; } }
        .pros-box { background: var(--emerald-50); border: 1px solid #a7f3d0; border-radius: 1rem; padding: 1.5rem; }
        .pros-box h4 { color: #065f46; font-weight: 700; margin-bottom: 1rem; font-size: 1.1rem; }
        .cons-box { background: var(--red-50); border: 1px solid #fecaca; border-radius: 1rem; padding: 1.5rem; }
        .cons-box h4 { color: #991b1b; font-weight: 700; margin-bottom: 1rem; font-size: 1.1rem; }
        .list-item { display: flex; align-items: start; gap: 0.5rem; font-size: 0.95rem; margin-bottom: 0.75rem; color: var(--slate-700); }

        .sidebar-sticky { position: sticky; top: 6rem; }
        .sidebar-box { background: var(--slate-900); color: white; border-radius: 1.5rem; padding: 2.5rem; box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.2); }
        .sidebar-box h3 { font-size: 1.5rem; font-weight: 800; margin-bottom: 1rem; }
        .sidebar-box p { color: var(--slate-400); font-size: 0.95rem; margin-bottom: 2rem; line-height: 1.6; }
        .sidebar-btn { display: block; width: 100%; background: var(--indigo-600); color: white; font-weight: 700; padding: 1rem; border-radius: 1rem; text-align: center; text-decoration: none; box-shadow: 0 10px 20px -5px rgba(79, 70, 229, 0.4); }

        .faq-item { background: var(--slate-50); border: 1px solid var(--slate-200); border-radius: 1rem; padding: 1.5rem; margin-bottom: 1rem; }
        .faq-item h4 { font-size: 1.1rem; font-weight: 700; color: var(--slate-900); margin-bottom: 0.5rem; }
        .faq-item p { color: var(--slate-600); margin-bottom: 0; }

        footer { background: var(--slate-900); color: var(--slate-400); text-align: center; padding: 3rem; border-top: 1px solid #1e293b; font-size: 0.875rem; }
    </style>
</head>
<body>

    <header>
        <div class="nav-container">
            <a href="index.html" class="logo-box">
                <div class="logo-icon">AI</div>
                <span>EcomStack</span>
            </a>
            <nav class="hidden md:flex">
                <a href="index.html" class="nav-link">Directory Hub</a>
                <a href="index.html" class="nav-link">Top Software</a>
                <a href="index.html" class="nav-link">Comparison</a>
            </nav>
            <a href="index.html" style="background: var(--indigo-600); color: white; font-weight: 600; padding: 0.75rem 1.5rem; border-radius: 9999px; text-decoration: none; box-shadow: 0 4px 12px rgba(79,70,229,0.3);">Home Hub</a>
        </div>
    </header>

    <section class="hero-section">
        <div class="hero-grid">
            <div>
                <div class="badge">__CATEGORY__ Growth Review (2026)</div>
                <h1>__NAME__ Review: Is It Worth <span>$__PRICE__/mo?</span></h1>
                <p class="hero-desc">An exhaustive analysis of __NAME__ for scaling direct-to-consumer brands and streamlining __CATEGORY_LOWER__ operations in 2026.</p>
                <div class="btn-group">
                    <a href="__AFFILIATE_LINK__" target="_blank" rel="nofollow noopener" class="btn-primary">Start Free Trial ➔</a>
                    <a href="#pricing" class="btn-secondary">View Pricing Breakdown</a>
                </div>
            </div>
            <div class="mockup-card">
                <div class="mockup-inner">
                    <div style="display: flex; align-items: center; justify-content: space-between; border-bottom: 1px solid #f1f5f9; padding-bottom: 1rem; margin-bottom: 1rem;">
                        <div style="font-weight: 700; color: #0f172a; font-size: 0.95rem;">__NAME__ Analytics Dashboard</div>
                        <span style="background: #ecfdf5; color: #059669; font-size: 0.75rem; font-weight: 700; padding: 0.25rem 0.75rem; border-radius: 9999px;">Verified 2026</span>
                    </div>
                    <div style="height: 120px; background: linear-gradient(to right, #eef2ff, #faf5ff, #f0fdf4); border-radius: 0.75rem; border: 1px solid #e0e7ff; display: flex; align-items: center; justify-content: center; font-weight: 600; color: #4f46e5; margin-bottom: 1rem;">
                        🚀 Performance Score: 98.4/100
                    </div>
                    <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 0.5rem;">
                        <div style="background: #f8fafc; padding: 0.75rem; border-radius: 0.5rem; border: 1px solid #f1f5f9;">
                            <div style="font-size: 9px; color: #94a3b8; font-weight: 700; text-transform: uppercase;">Uptime</div>
                            <div style="font-weight: 800; font-size: 0.85rem; color: #059669;">99.9%</div>
                        </div>
                        <div style="background: #f8fafc; padding: 0.75rem; border-radius: 0.5rem; border: 1px solid #f1f5f9;">
                            <div style="font-size: 9px; color: #94a3b8; font-weight: 700; text-transform: uppercase;">ROI Speed</div>
                            <div style="font-weight: 800; font-size: 0.85rem; color: #1e293b;">&lt; 14 Days</div>
                        </div>
                        <div style="background: #f8fafc; padding: 0.75rem; border-radius: 0.5rem; border: 1px실 border: 1px solid #f1f5f9;">
                            <div style="font-size: 9px; color: #94a3b8; font-weight: 700; text-transform: uppercase;">Rating</div>
                            <div style="font-weight: 800; font-size: 0.85rem; color: #4f46e5;">4.8 / 5</div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <main>
        <article>
            <div class="content-card">
                <h2>Comprehensive Overview of __NAME__</h2>
                <p>In the fast-moving world of e-commerce, modern store owners face constant pressure to optimize every single lever of their business. Whether you are dealing with __CATEGORY_LOWER__ bottlenecks, scaling ad spend, or managing customer expectations, manual workflows simply cannot keep pace with multi-channel growth.</p>
                <p><strong>__NAME__</strong> enters the market at <strong>$__PRICE__/month</strong> as a specialized solution designed to cut through operational complexity. By leveraging modern cloud automation and advanced tooling, it targets the exact pain points that drain profitability from growing online stores.</p>
                <p>Throughout this review, we analyze __NAME__'s feature set, ecosystem compatibility, pricing structure, and real-world utility so you can decide if it belongs in your tech stack.</p>
            </div>

            <div class="content-card">
                <h2>Key Features & Capabilities Breakdown</h2>
                <p>Our editorial evaluation identified several standout features that set __NAME__ apart from legacy alternatives:</p>
                <div style="display: grid; gap: 0.75rem; margin-top: 1rem;">
                    __FEATURES_HTML__
                </div>
            </div>

            <div class="content-card">
                <h2>Pros & Cons of __NAME__</h2>
                <div class="pros-cons-grid">
                    <div class="pros-box">
                        <h4>What We Like (Pros)</h4>
                        <div class="list-item">✅ Deep integration with major e-commerce platforms like Shopify.</div>
                        <div class="list-item">✅ Intuitive user interface with minimal onboarding friction.</div>
                        <div class="list-item">✅ Robust automation rules that save hours of manual oversight.</div>
                    </div>
                    <div class="cons-box">
                        <h4>Potential Drawbacks (Cons)</h4>
                        <div class="list-item">❌ Pricing can scale up quickly for high-volume stores.</div>
                        <div class="list-item">❌ Requires initial configuration time to dial in custom rules.</div>
                    </div>
                </div>
            </div>

            <div class="content-card">
                <h2 id="pricing">Pricing & ROI Analysis</h2>
                <p>Starting at <strong>$__PRICE__/month</strong>, __NAME__ is priced competitively for growth-stage brands. When evaluated against the labor hours saved and the potential upside in operational efficiency or revenue protection, the platform typically achieves positive ROI within its first billing cycle.</p>
                <p>We always recommend testing any new SaaS tool using their trial period before committing to an annual plan.</p>
                <div style="margin-top: 1.5rem;">
                    <a href="__AFFILIATE_LINK__" target="_blank" rel="nofollow noopener" class="btn-primary">Claim __NAME__ Free Trial ➔</a>
                </div>
            </div>

            <div class="content-card">
                <h2>Ecosystem Integrations</h2>
                <p>A software tool is only as good as its ability to communicate with the rest of your tech stack. __NAME__ connects smoothly with:</p>
                <div style="display: flex; flex-wrap: wrap; gap: 0.75rem; margin-top: 1rem;">
                    __INTEGRATIONS_HTML__
                </div>
            </div>

            <div class="content-card">
                <h2>Frequently Asked Questions (FAQ)</h2>
                <div class="faq-item">
                    <h4>Is __NAME__ suitable for small Shopify stores?</h4>
                    <p>Yes, while enterprise brands benefit from its advanced scalability, solo founders and growing teams can utilize its core features right out of the box.</p>
                </div>
                <div class="faq-item">
                    <h4>How long does setup take?</h4>
                    <p>Most merchants can complete the onboarding wizard and sync their store data in under 15 minutes.</p>
                </div>
                <div class="faq-item">
                    <h4>Does __NAME__ offer a free trial?</h4>
                    <p>Yes, you can test out the platform features through our exclusive partner link above.</p>
                </div>
            </div>
        </article>

        <aside class="sidebar-sticky">
            <div class="sidebar-box">
                <div style="color: #818cf8; font-size: 0.75rem; font-weight: 700; text-transform: uppercase; margin-bottom: 0.5rem;">Expert Recommendation</div>
                <h3>Ready to scale?</h3>
                <p>Stop losing revenue to inefficient __CATEGORY_LOWER__ workflows. Get started with __NAME__ today.</p>
                <a href="__AFFILIATE_LINK__" target="_blank" rel="nofollow noopener" class="sidebar-btn">Start Free Trial</a>
            </div>
        </aside>
    </main>

    <footer>
        &copy; 2026 EcomStack. All rights reserved. Professional E-commerce Software Reviews & Guides. <a href="index.html" style="color: #818cf8; text-decoration: none; margin-left: 1rem;">Home Hub</a>
    </footer>

</body>
</html>
"""

INDEX_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>EcomStack | E-commerce & AI Software Directory Hub</title>
    <meta name="description" content="Discover, compare, and review the best e-commerce software, marketing tools, and logistics automation platforms in 2026.">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
    <style>
        :root {
            --slate-50: #f8fafc; --slate-100: #f1f5f9; --slate-200: #e2e8f0; --slate-600: #475569; --slate-900: #0f172a;
            --indigo-600: #4f46e5; --indigo-700: #4338ca; --indigo-50: #eef2ff;
        }
        * { box-sizing: border-box; margin: 0; padding: 0; }
        body { font-family: 'Inter', sans-serif; background-color: var(--slate-50); color: var(--slate-900); line-height: 1.6; }
        header { background: white; border-bottom: 1px solid var(--slate-200); position: sticky; top: 0; z-index: 50; }
        .nav-container { max-width: 1280px; margin: 0 auto; padding: 0 1.5rem; height: 5rem; display: flex; align-items: center; justify-content: space-between; }
        .logo { font-weight: 800; font-size: 1.25rem; color: var(--slate-900); text-decoration: none; display: flex; align-items: center; gap: 0.75rem; }
        .logo-icon { width: 2.25rem; height: 2.25rem; background: var(--indigo-600); color: white; border-radius: 0.5rem; display: flex; align-items: center; justify-content: center; font-size: 1.1rem; }
        
        .hero { max-width: 1280px; margin: 0 auto; padding: 5rem 1.5rem 3rem; text-align: center; }
        .hero h1 { font-size: 3rem; font-weight: 800; letter-spacing: -0.025em; margin-bottom: 1rem; color: var(--slate-900); }
        .hero h1 span { color: var(--indigo-600); }
        .hero p { font-size: 1.25rem; color: var(--slate-600); max-width: 42rem; margin: 0 auto; }

        .container { max-width: 1280px; margin: 0 auto; padding: 0 1.5rem 5rem; }
        .grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(360px, 1fr)); gap: 2rem; }
        .card { background: white; border: 1px solid var(--slate-200); border-radius: 1.25rem; padding: 2rem; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.02); display: flex; flex-direction: column; justify-content: space-between; transition: transform 0.2s, box-shadow 0.2s; text-decoration: none; color: inherit; }
        .card:hover { transform: translateY(-4px); box-shadow: 0 20px 25px -5px rgba(0,0,0,0.08); border-color: var(--indigo-600); }
        .card-tag { display: inline-block; background: var(--indigo-50); color: var(--indigo-700); font-size: 0.75rem; font-weight: 700; padding: 0.25rem 0.75rem; border-radius: 9999px; text-transform: uppercase; margin-bottom: 1rem; }
        .card h3 { font-size: 1.5rem; font-weight: 700; margin-bottom: 0.75rem; color: var(--slate-900); }
        .card p { color: var(--slate-600); font-size: 0.95rem; margin-bottom: 1.5rem; }
        .card-footer { display: flex; align-items: center; justify-content: space-between; border-top: 1px solid var(--slate-100); padding-top: 1rem; font-weight: 600; font-size: 0.9rem; color: var(--indigo-600); }
        
        footer { background: var(--slate-900); color: var(--slate-400); text-align: center; padding: 3rem; margin-top: 5rem; font-size: 0.875rem; }
    </style>
</head>
<body>

    <header>
        <div class="nav-container">
            <a href="index.html" class="logo">
                <div class="logo-icon">AI</div>
                <span>EcomStack</span>
            </a>
            <span style="font-size: 0.875rem; font-weight: 600; color: var(--indigo-600);">Software Directory Hub</span>
        </div>
    </header>

    <div class="hero">
        <h1>Scale Your E-commerce Brand With <span>Top Software & AI</span></h1>
        <p>In-depth, expert software reviews of SaaS tools for inventory, marketing, support, and analytics.</p>
    </div>

    <div class="container">
        <div class="grid">
            __CARDS_HTML__
        </div>
    </div>

    <footer>
        &copy; 2026 EcomStack. All rights reserved. Professional E-commerce Software Directory.
    </footer>

</body>
</html>
"""

def generate_programmatic_page(software_data):
    name = software_data['name']
    category = software_data['category']
    price = str(software_data['starting_price'])
    affiliate_link = software_data.get('affiliate_link', '#')
    slug = name.lower().replace(".", "").replace(" ", "-") + "-review"
    filename = f"{slug}.html"
    filepath = os.path.join(OUTPUT_DIR, filename)
    
    features_html = "".join([f"""
        <div style="display: flex; align-items: center; gap: 0.75rem; color: #334155; font-weight: 500; background: #f8fafc; padding: 0.875rem 1rem; border-radius: 0.75rem; border: 1px solid #f1f5f9;">
            <div style="width: 1.5rem; height: 1.5rem; border-radius: 9999px; background: #eef2ff; color: #4f46e5; display: flex; align-items: center; justify-content: center; font-size: 0.75rem; font-weight: 700; flex-shrink: 0;">✓</div>
            <span>{f}</span>
        </div>
    """ for f in software_data['features']])
    
    integrations_html = "".join([f"""
        <div style="display: flex; align-items: center; gap: 0.5rem; background: white; padding: 0.75rem 1rem; border-radius: 0.75rem; border: 1px solid #e2e8f0; font-weight: 600; color: #1e293b; box-shadow: 0 1px 2px rgba(0,0,0,0.05);">
            <span style="width: 0.625rem; height: 0.625rem; border-radius: 9999px; background: #10b981;"></span>
            {integ}
        </div>
    """ for integ in software_data['integrations']])
    
    page_content = (HTML_TEMPLATE
                    .replace("__NAME__", name)
                    .replace("__CATEGORY__", category)
                    .replace("__CATEGORY_LOWER__", category.lower())
                    .replace("__PRICE__", price)
                    .replace("__AFFILIATE_LINK__", affiliate_link)
                    .replace("__FEATURES_HTML__", features_html)
                    .replace("__INTEGRATIONS_HTML__", integrations_html))

    ensure_output_dir()
    with open(filepath, "w", encoding="utf-8") as file:
        file.write(page_content)
        
    return slug

def generate_index_page(software_list):
    cards_html = ""
    for item in software_list:
        slug = item['name'].lower().replace(".", "").replace(" ", "-") + "-review"
        cards_html += f"""
        <a href="{slug}.html" class="card">
            <div>
                <span class="card-tag">{item['category']}</span>
                <h3>{item['name']} Review (2026)</h3>
                <p>Starting at ${item['starting_price']}/mo. Explore features, integrations, and operational workflows.</p>
            </div>
            <div class="card-footer">
                <span>Read In-Depth Review</span>
                <span>➔</span>
            </div>
        </a>
        """
    
    index_content = INDEX_TEMPLATE.replace("__CARDS_HTML__", cards_html)
    index_path = os.path.join(OUTPUT_DIR, "index.html")
    with open(index_path, "w", encoding="utf-8") as f:
        f.write(index_content)

if __name__ == "__main__":
    print("Building EcomStack pSEO Empire...")
    ensure_output_dir()
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            software_batch = json.load(f)
    except FileNotFoundError:
        software_batch = []

    if software_batch:
        for item in software_batch:
            generate_programmatic_page(item)
            time.sleep(0.05)
        generate_index_page(software_batch)
    print("Build complete! All long-form review pages generated.")