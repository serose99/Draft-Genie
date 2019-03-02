   def start_html():
        return '<html>'

    def end_html():
        return '</html>'

    def print_html(text):
        text = str(text)
        text = text.replace('\n', '<br>')
        return '<p>' + str(text) + '</p>'
if __name__ == '__main__':
        webpage_data =  start_html()
        webpage_data += print_html("Hi Welcome to Python test page\n")
        webpage_data += fd.write(print_html("Now it will show a calculation"))
        webpage_data += print_html("30+2=")
        webpage_data += print_html(30+2)
        webpage_data += end_html()
        with open('index.html', 'w') as fd: fd.write(webpage_data)