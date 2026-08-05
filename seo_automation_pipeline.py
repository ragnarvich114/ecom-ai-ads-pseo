import json
import os
import time

OUTPUT_DIR = "./public"

def ensure_output_dir():
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en" style="scroll-behavior: smooth;">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>__NAME__ Review (2026): Is It Worth $__PRICE__/mo? | EcomStack AI</title>
    <meta name="description" content="An in-depth review of __NAME__. We analyze its AI capabilities, pricing, workflows, and integrations for modern E-commerce and Meta/TikTok Ad buyers.">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
    <style>
        :root {
            --slate-50: #f8fafc; --slate-100: #f1f5f9; --slate-200: #e2e8f0; --slate-400: #94a3b8;
            --slate-600: #475569; --slate-700: #334155; --slate-800: #1e293b; --slate-900: #0f172a;
            --indigo-50: #eef2ff; --indigo-100: #e0e7ff; --indigo-600: #4f46e5; --indigo-700: #4338ca;
            --emerald-50: #ecfdf5; --emerald-600: #059669;
        }
        * { box-sizing: border-box; margin: 0; padding: 0; }
        body { font-family: 'Inter', sans-serif; background-color: var(--slate-50); color: var(--slate-800); line-height: 1.6; min-height: 100vh; display: flex; flex-direction: column; justify-content: space-between; }
        
        header { position: sticky; top: 0; z-index: 50; background: rgba(255, 255, 255, 0.9); backdrop-filter: blur(12px); border-bottom: 1px solid rgba(226, 232, 240, 0.8); }
        .nav-container { max-width: 1280px; margin: 0 auto; padding: 0 1.5rem; height: 5rem; display: flex; align-items: center; justify-content: space-between; }
        .logo-box { display: flex; align-items: center; gap: 0.75rem; font-weight: 800; font-size: 1.25rem; color: var(--slate-900); text-decoration: none; }
        .logo-icon { width: 2.25rem; height: 2.25rem; background: var(--indigo-600); color: white; border-radius: 0.5rem; display: flex; align-items: center; justify-content: center; font-size: 1.1rem; box-shadow: 0 4px 12px rgba(79, 70, 229, 0.3); }
        
        nav { display: flex; gap: 1.75rem; align-items: center; font-weight: 500; font-size: 0.875rem; color: var(--slate-700); }
        .nav-link { color: var(--slate-700); text-decoration: none; transition: color 0.2s; }
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
        .content-card p { color: var(--slate-600); font-size: 1rem; line-height: 1.7; margin-bottom: 1.5rem; }

        .sidebar-sticky { position: sticky; top: 6rem; }
        .sidebar-box { background: var(--slate-900); color: white; border-radius: 1.5rem; padding: 2.5rem; box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.2); }
        .sidebar-box h3 { font-size: 1.5rem; font-weight: 800; margin-bottom: 1rem; }
        .sidebar-box p { color: var(--slate-400); font-size: 0.95rem; margin-bottom: 2rem; line-height: 1.6; }
        .sidebar-btn { display: block; width: 100%; background: var(--indigo-600); color: white; font-weight: 700; padding: 1rem; border-radius: 1rem; text-align: center; text-decoration: none; box-shadow: 0 10px 20px -5px rgba(79, 70, 229, 0.4); }

        .banner-section { max-width: 1280px; margin: 0 auto 4rem; padding: 0 1.5rem; width: 100%; }
        .banner-box { background: linear-gradient(135deg, #1e1b4b, #312e81, #0f172a); border-radius: 1.5rem; padding: 3rem; color: white; display: flex; align-items: center; justify-content: space-between; gap: 2rem; box-shadow: 0 25px 50px -12px rgba(15, 23, 42, 0.3); flex-wrap: wrap; }
        
        footer { background: var(--slate-900); color: var(--slate-400); text-align: center; padding: 3rem; border-top: 1px solid #1e293b; font-size: 0.875rem; }
    </style>
</head>
<body>

    <header>
        <div class="nav-container">
            <a href="/" class="logo-box">
                <div class="logo-icon">AI</div>
                <span>EcomStack AI</span>
            </a>
            <nav>
                <a href="/" class="nav-link">Home Hub</a>
                <a href="#pricing" class="nav-link">Top Tools</a>
            </nav>
            <a href="/" style="background: var(--indigo-600); color: white; font-weight: 600; padding: 0.75rem 1.5rem; border-radius: 9999px; text-decoration: none; box-shadow: 0 4px 12px rgba(79,70,229,0.3);">Explore Deals</a>
        </div>
    </header>

    <section class="hero-section">
        <div class="hero-grid">
            <div>
                <div class="badge">__CATEGORY__ Intelligence Review</div>
                <h1>__NAME__ Review (2026): Is It Worth <span>$__PRICE__/mo?</span></h1>
                <p class="hero-desc">__NAME__ is an essential AI-powered platform designed to streamline __CATEGORY_LOWER__ operations and accelerate business growth.</p>
                <div class="btn-group">
                    <a href="#" class="btn-primary">Start Free Trial ➔</a>
                    <a href="#pricing" class="btn-secondary">View Pricing Details</a>
                </div>
            </div>
            <div class="mockup-card">
                <div class="mockup-inner">
                    <div style="display: flex; align-items: center; justify-content: space-between; border-bottom: 1px solid #f1f5f9; padding-bottom: 1rem; margin-bottom: 1rem;">
                        <div style="font-weight: 700; color: #0f172a; font-size: 0.95rem;">__NAME__ Control Hub</div>
                        <span style="background: #ecfdf5; color: #059669; font-size: 0.75rem; font-weight: 700; padding: 0.25rem 0.75rem; border-radius: 9999px;">Verified 2026</span>
                    </div>
                    <div style="height: 120px; background: linear-gradient(to right, #eef2ff, #faf5ff, #f0fdf4); border-radius: 0.75rem; border: 1px solid #e0e7ff; display: flex; align-items: center; justify-content: center; font-weight: 600; color: #4f46e5; margin-bottom: 1rem;">
                        AI Model Synchronized
                    </div>
                    <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 0.5rem;">
                        <div style="background: #f8fafc; padding: 0.75rem; border-radius: 0.5rem; border: 1px solid #f1f5f9;">
                            <div style="font-size: 9px; color: #94a3b8; font-weight: 700; text-transform: uppercase;">Status</div>
                            <div style="font-weight: 800; font-size: 0.85rem; color: #059669;">Active</div>
                        </div>
                        <div style="background: #f8fafc; padding: 0.75rem; border-radius: 0.5rem; border: 1px solid #f1f5f9;">
                            <div style="font-size: 9px; color: #94a3b8; font-weight: 700; text-transform: uppercase;">Uptime</div>
                            <div style="font-weight: 800; font-size: 0.85rem; color: #1e293b;">99.9%</div>
                        </div>
                        <div style="background: #f8fafc; padding: 0.75rem; border-radius: 0.5rem; border: 1px solid #f1f5f9;">
                            <div style="font-size: 9px; color: #94a3b8; font-weight: 700; text-transform: uppercase;">ROI Boost</div>
                            <div style="font-weight: 800; font-size: 0.85rem; color: #4f46e5;">3.4x</div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <main>
        <article>
            <div class="content-card">
                <h2>Overview</h2>
                <p>Deploying advanced __CATEGORY_LOWER__ tools is no longer optional for scaling teams. Today we review <strong>__NAME__</strong>, starting at <strong>$__PRICE__/month</strong>, to evaluate its real-world performance and affiliate value.</p>
            </div>

            <div class="content-card">
                <h2>Key Features & AI Capabilities</h2>
                <div style="display: grid; gap: 0.75rem; margin-top: 1rem;">
                    __FEATURES_HTML__
                </div>
            </div>

            <div class="content-card">
                <h2>Ecosystem Integrations</h2>
                <p>Seamlessly plugs into your current technology stack:</p>
                <div style="display: flex; flex-wrap: wrap; gap: 0.75rem; margin-top: 1rem;">
                    __INTEGRATIONS_HTML__
                </div>
            </div>
        </article>

        <aside class="sidebar-sticky">
            <div class="sidebar-box">
                <div style="color: #818cf8; font-size: 0.75rem; font-weight: 700; text-transform: uppercase; margin-bottom: 0.5rem;">Recommended Tool</div>
                <h3>Ready to upgrade?</h3>
                <p>Claim your trial access for __NAME__ and streamline your operations today.</p>
                <a href="#" class="sidebar-btn">Start Free Trial</a>
            </div>
        </aside>
    </main>

    <div class="banner-section">
        <div class="banner-box">
            <div>
                <h2 style="font-size: 2rem; font-weight: 800; margin-bottom: 0.5rem;">Scale your __CATEGORY_LOWER__ stack today</h2>
                <p style="color: #c7d2fe; font-size: 1rem;">Join leading companies leveraging __NAME__ for automated growth and efficiency.</p>
            </div>
            <a href="#" style="background: linear-gradient(135deg, #2dd4bf, #38bdf8); color: #0f172a; font-weight: 800; padding: 1rem 2rem; border-radius: 1rem; text-decoration: none; box-shadow: 0 10px 25px rgba(45, 212, 191, 0.3); white-space: nowrap;">Claim Your Trial Now ➔</a>
        </div>
    </div>

    <footer>
        &copy; 2026 EcomStack AI. All rights reserved.
    </footer>

</body>
</html>
"""

INDEX_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>EcomStack AI | E-commerce & Dropshipping AI Ads Software Directory</title>
    <meta name="description" content="Discover and compare the best AI ad generators, Meta & TikTok automation tools, and e-commerce analytics platforms for scaling your DTC brand.">
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
            <a href="/" class="logo">
                <div class="logo-icon">AI</div>
                <span>EcomStack AI</span>
            </a>
            <span style="font-size: 0.875rem; font-weight: 600; color: var(--indigo-600);">Meta & TikTok Ad Tech Directory</span>
        </div>
    </header>

    <div class="hero">
        <h1>Scale Your DTC Brand With <span>AI & Automated Ads</span></h1>
        <p>In-depth, programmatic reviews of the top SaaS tools for Meta ad scaling, TikTok creatives, dropshipping analytics, and workflows.</p>
    </div>

    <div class="container">
        <div class="grid">
            __CARDS_HTML__
        </div>
    </div>

    <footer>
        &copy; 2026 EcomStack AI. All rights reserved. Programmatic SEO Engine.
    </footer>

</body>
</html>
"""

def generate_programmatic_page(software_data):
    name = software_data['name']
    category = software_data['category']
    price = str(software_data['starting_price'])
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
    
    page_content = HTML_TEMPLATE.replace("__NAME__", name).replace("__CATEGORY__", category).replace("__CATEGORY_LOWER__", category.lower()).replace("__PRICE__", price).replace("__FEATURES_HTML__", features_html).replace("__INTEGRATIONS_HTML__", integrations_html)

    ensure_output_dir()
    with open(filepath, "w", encoding="utf-8") as file:
        file.write(page_content)
        
    print(f"[+] Generated review page: {filename}")
    return slug

def generate_index_page(software_list):
    cards_html = ""
    for item in software_list:
        slug = item['name'].lower().replace(".", "").replace(" ", "-") + "-review"
        cards_html += f"""
        <a href="/{slug}.html" class="card">
            <div>
                <span class="card-tag">{item['category']}</span>
                <h3>{item['name']} Review (2026)</h3>
                <p>Starting at ${item['starting_price']}/mo. Explore AI features, Meta & TikTok integrations, and workflow automation.</p>
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
    print("[+] Generated homepage directory hub: index.html")

if __name__ == "__main__":
    ecom_ai_ads_batch = [
        {
            "name": "AdCreative.ai",
            "category": "AI Ad Creatives",
            "starting_price": 29,
            "features": ["AI banner & video generation", "Competitor ad intelligence", "Platform-specific sizing (Meta/TikTok)", "Conversion score prediction"],
            "integrations": ["Meta Ads", "TikTok Ads", "Shopify", "Google Ads"]
        },
        {
            "name": "Madgicx",
            "category": "Meta & TikTok Ad Automation",
            "starting_price": 49,
            "features": ["AI ad launcher & media buying", "Ad spy & creative intelligence", "Automated budget rules", "Cross-channel ROAS dashboard"],
            "integrations": ["Meta Ads Manager", "TikTok Ads", "Shopify"]
        },
        {
            "name": "Triple Whale",
            "category": "Analytics & Attribution",
            "starting_price": 100,
            "features": ["Centralized AI attribution", "P&L dashboard", "Creative analytics", "First-party pixel tracking"],
            "integrations": ["Shopify", "Meta Ads", "Google Ads", "TikTok Ads"]
        },
        {
            "name": "Ringly.io",
            "category": "Voice & Support Agents",
            "starting_price": 349,
            "features": ["Autonomous AI phone agent", "Instant order tracking lookup", "Automated returns & exchanges", "24/7 voice routing"],
            "integrations": ["Shopify", "Twilio", "Zapier"]
        },
        {
            "name": "Make.com",
            "category": "Workflow Automation",
            "starting_price": 9,
            "features": ["Visual scenario builder", "Advanced data mapping", "Error handling modules", "Real-time execution logs"],
            "integrations": ["OpenAI", "Slack", "HubSpot", "Google Sheets"]
        },
        {
            "name": "Gorgias",
            "category": "Customer Support",
            "starting_price": 60,
            "features": ["Unified helpdesk", "AI macros and auto-responses", "Order tracking self-service", "Live chat widgets"],
            "integrations": ["Shopify", "Magento", "Recharge"]
        }
    ]

    print("="*50)
    print("BUILDING E-COMMERCE AI ADS pSEO EMPIRE")
    print("="*50)
    
    ensure_output_dir()
    for item in ecom_ai_ads_batch:
        generate_programmatic_page(item)
        time.sleep(0.2)
        
    generate_index_page(ecom_ai_ads_batch)

    print("="*50)
    print("BUILD COMPLETE! Homepage hub and review pages compiled in /public/")
    print("="*50)