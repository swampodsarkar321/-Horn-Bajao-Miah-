import re
p = r"c:\Users\SWAMPOD\Downloads\baper-rasta.html"
s = open(p, encoding="utf-8").read()
i = s.rfind("<script")
j = s.rfind("</script>")
code = s[i:j+len("</script>")]
code = re.sub(r"(?s)^.*?<script[^>]*>", "", code)
code = re.sub(r"</script>.*$", "", code)
open(r"c:\Users\SWAMPOD\Downloads\_check.js", "w", encoding="utf-8").write(code)
print("done", len(code))