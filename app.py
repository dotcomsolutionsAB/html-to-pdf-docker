from flask import Flask, request, make_response
import pdfkit  # You can also use WeasyPrint if you prefer.

app = Flask(__name__)

@app.route('/html-to-pdf', methods=['POST'])
def html_to_pdf():
    content = request.json.get('html')
    if not content:
        return {"error": "No HTML content provided"}, 400

    # Generate PDF from HTML
    pdf = pdfkit.from_string(content, False)

    # Create a PDF response
    response = make_response(pdf)
    response.headers['Content-Type'] = 'application/pdf'
    response.headers['Content-Disposition'] = 'inline; filename=document.pdf'

    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
