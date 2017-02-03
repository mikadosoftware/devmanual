f = 'example-page.tmpl'
txt = open(f).read().decode("utf-8")
html = txt % {'bootstrappath': 'bootstrap/dist/',
              'fontawesomepath': 'bootstrap/dist/',
              'jquerypath': 'bootstrap/dist/',              
              
}
print html
