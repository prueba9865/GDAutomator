import webbrowser, sys

# Dominio objetivo
target = sys.argv[1]

# Lista de Google Dorks
dorks = [
    # Documentos / scripts / código / macros
    'site:{} (ext:doc | ext:docx | ext:odt | ext:rtf | ext:sxw | ext:psw | ext:ppt | ext:pptx | ext:pps | ext:csv | ext:xlsm | ext:docm | ext:sh | ext:bat | ext:ps1 | ext:cmd | ext:java | ext:py | ext:js | ext:rb | ext:c | ext:cpp | ext:html | ext:htm | ext:css | ext:ts | ext:vue)',

    # Directorios expuestos
    'site:{} intitle:"index of"',

    # Certificados y claves
    'site:{} (ext:pem | ext:crt | ext:key | ext:csr | ext:der | ext:jks | ext:p12 | ext:keystore | intext:"BEGIN RSA PRIVATE KEY" | intext:"ssh-rsa")',

    # Archivos de configuración y secrets
    'site:{} (ext:xml | ext:conf | ext:cnf | ext:reg | ext:inf | ext:rdp | ext:cfg | ext:txt | ext:ora | ext:ini | ext:env | ext:toml | ext:properties | ext:yml | ext:yaml | ext:json | intext:"token=" | intext:"password=" | intext:"passwd=" | intext:"credentials=" | intext:"API_KEY=" | intext:"SECRET_KEY" | intext:"access_token" | intext:"AWS_SECRET_ACCESS_KEY" | intext:"AWS_ACCESS_KEY_ID" | intext:"GCP_PRIVATE_KEY" | intext:"DOCKER_HUB_PASSWORD")',

    # Bases de datos / backups / logs
    'site:{} (ext:sql | ext:dbf | ext:mdb | ext:accdb | ext:sqlite | ext:sqlite3 | ext:db | ext:bkf | ext:bkp | ext:bak | ext:old | ext:backup | ext:zip | ext:rar | ext:7z | ext:gz | ext:tar | ext:log | ext:access | ext:error | ext:trace | ext:err | ext:audit | ext:security | ext:evt | ext:evtx)',

    # Login / autenticación / paneles / dashboards
    'site:{} (inurl:login | inurl:signin | intitle:Login | intitle:"sign in" | inurl:auth | inurl:signup | inurl:register | intitle:Signup | inurl:wp-admin | inurl:cpanel | inurl:phpmyadmin | intitle:"phpMyAdmin" | inurl:grafana | inurl:kibana | inurl:prometheus | inurl:graylog | inurl:jenkins | intitle:"Dashboard [Jenkins]")',

    # Errores y vulnerabilidades
    'site:{} (intext:"sql syntax near" | intext:"syntax error has occurred" | intext:"incorrect syntax near" | intext:"unexpected end of SQL command" | intext:"Warning: mysql_connect()" | intext:"Warning: mysql_query()" | intext:"Warning: pg_connect()" | "PHP Parse error" | "PHP Warning" | "PHP Error" | "Index of /" | "wp-content" | "Django error" | "Traceback (most recent call last)" | "Laravel" | "APP_KEY=")',

    # Archivos phpinfo
    'site:{} ext:php intitle:phpinfo "published by the PHP Group"',

    # Pastebins y similares
    'site:(pastebin.com | paste2.org | pastehtml.com | slexy.org | snipplr.com | snipt.net | textsnip.com | bitpaste.app | justpaste.it | heypasteit.com | hastebin.com | dpaste.org | dpaste.com | codepad.org | jsitor.com | codepen.io | jsfiddle.net | dotnetfiddle.net | phpfiddle.org | ide.geeksforgeeks.org | repl.it | ideone.com | paste.debian.net | paste.org | paste.org.ru | codebeautify.org | codeshare.io | trello.com) "{}"',

    # Repositorios de código
    'site:(github.com | gitlab.com) "{}"',

    # Ficheros .git expuestos
    'inurl:".git/config" site:{}',

    # Información filtrada en cloud
    'site:(drive.google.com | dropbox.com | onedrive.live.com | trello.com | atlassian.net | s3.amazonaws.com | blob.core.windows.net | storage.googleapis.com) "{}"',

    # StackOverflow
    'site:stackoverflow.com "{}"',

    # Subdominios
    'site:*.{}',
    'site:*.*.{}',

    # Elastic / Mongo / Kibana expuestos
    'site:{} ("kibana" "Discover" | "MongoDB" "Server Information" | "Elasticsearch" "cluster")',

    # Docker / Kubernetes / CI-CD
    'site:{} (ext:Dockerfile | ext:docker-compose.yml | ext:circleci | ext:travis.yml | ext:github/workflows | intext:"kind: Pod" | intext:"apiVersion:")',

    # Dispositivos / IoT expuestos
    'site:{} (inurl:admin | inurl:setup | inurl:status | inurl:config)',

    # Frameworks / CMS
    'site:{} (ext:yml | ext:yaml | ext:json | ext:conf | ext:ini) "Drupal" | "Joomla" | "WordPress" | "framework" | "CMS"',
]

# Generar y abrir búsquedas
for dork in dorks:
    query = dork.format(target)
    url = f"https://www.google.com/search?q={query}"
    webbrowser.open_new_tab(url)