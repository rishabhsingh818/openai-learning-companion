#!/usr/bin/env python3
"""
Convert PROJECT_SUBMISSION.md to PDF
This script converts the Markdown submission to a professional PDF document
"""

import os
import sys

def convert_to_pdf():
    """Convert the submission markdown to PDF"""
    
    # Try different conversion methods
    conversion_methods = [
        # Method 1: Using pandoc (if available)
        "pandoc PROJECT_SUBMISSION.md -o PROJECT_SUBMISSION.pdf --pdf-engine=wkhtmltopdf",
        
        # Method 2: Using pandoc with different engine
        "pandoc PROJECT_SUBMISSION.md -o PROJECT_SUBMISSION.pdf",
        
        # Method 3: Using markdown-pdf (if installed)
        "markdown-pdf PROJECT_SUBMISSION.md",
    ]
    
    print("🔄 Attempting to convert PROJECT_SUBMISSION.md to PDF...")
    
    for i, method in enumerate(conversion_methods, 1):
        print(f"\n📄 Method {i}: {method}")
        try:
            result = os.system(method)
            if result == 0:
                print("✅ PDF conversion successful!")
                print(f"📋 Output file: PROJECT_SUBMISSION.pdf")
                return True
        except Exception as e:
            print(f"❌ Method {i} failed: {e}")
            continue
    
    print("\n⚠️  Direct PDF conversion not available.")
    print("\n🔄 Alternative options:")
    print("1. Install Pandoc: https://pandoc.org/installing.html")
    print("2. Use online converter: https://pandoc.org/try/")
    print("3. Copy content to Google Docs and export as PDF")
    print("4. Use VS Code with Markdown PDF extension")
    
    return False

def create_html_version():
    """Create an HTML version as fallback"""
    print("\n🌐 Creating HTML version as fallback...")
    
    try:
        with open('PROJECT_SUBMISSION.md', 'r', encoding='utf-8') as md_file:
            content = md_file.read()
        
        # Basic Markdown to HTML conversion
        html_content = f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>AI-Powered Learning Companion - Project Submission</title>
    <style>
        body {{ font-family: Arial, sans-serif; max-width: 900px; margin: 0 auto; padding: 20px; line-height: 1.6; }}
        h1 {{ color: #2c3e50; border-bottom: 2px solid #3498db; }}
        h2 {{ color: #34495e; border-bottom: 1px solid #bdc3c7; }}
        h3 {{ color: #7f8c8d; }}
        code {{ background-color: #f8f9fa; padding: 2px 4px; border-radius: 3px; }}
        pre {{ background-color: #f8f9fa; padding: 15px; border-radius: 5px; overflow-x: auto; }}
        table {{ border-collapse: collapse; width: 100%; }}
        th, td {{ border: 1px solid #ddd; padding: 12px; text-align: left; }}
        th {{ background-color: #f2f2f2; }}
        .emoji {{ font-size: 1.2em; }}
    </style>
</head>
<body>
<pre>{content.replace('<', '&lt;').replace('>', '&gt;')}</pre>
</body>
</html>
"""
        
        with open('PROJECT_SUBMISSION.html', 'w', encoding='utf-8') as html_file:
            html_file.write(html_content)
        
        print("✅ HTML version created: PROJECT_SUBMISSION.html")
        print("💡 You can open this in browser and use 'Print to PDF' option")
        return True
        
    except Exception as e:
        print(f"❌ HTML creation failed: {e}")
        return False

if __name__ == "__main__":
    print("📄 PROJECT SUBMISSION PDF CONVERTER")
    print("=" * 50)
    
    # Check if submission file exists
    if not os.path.exists('PROJECT_SUBMISSION.md'):
        print("❌ PROJECT_SUBMISSION.md not found!")
        sys.exit(1)
    
    # Try PDF conversion
    pdf_success = convert_to_pdf()
    
    # Create HTML fallback
    if not pdf_success:
        create_html_version()
    
    print("\n🎯 SUBMISSION FILES READY:")
    print("📋 PROJECT_SUBMISSION.md - Original Markdown")
    
    if os.path.exists('PROJECT_SUBMISSION.pdf'):
        print("📄 PROJECT_SUBMISSION.pdf - PDF version")
    
    if os.path.exists('PROJECT_SUBMISSION.html'):
        print("🌐 PROJECT_SUBMISSION.html - HTML version (print to PDF)")
    
    print("\n🚀 Your professional submission is ready!")