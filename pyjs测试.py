import execjs
print(execjs.get().name)  # 这将打印出你当前的 JavaScript 运行环境，例如 Node.js (V8)

jstext = "function hello(str){return str;}"
ctx = execjs.compile(jstext)
a = ctx.call("hello", " hello world")
print(a)