import gh_md_to_html
f = open("test.md","r").read()
print(gh_md_to_html.core_converter.markdown(f))