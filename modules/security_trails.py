import re
import json

from core.requester import requester

def security_trails(domain):
	response = requester(
		f'https://securitytrails.com/list/apex_domain/{domain}'
	).text
	prefixes = json.loads(re.search(r'(?m)"subdomains":(\[.*?\])', response)[1])
	return [f'{prefix}.{domain}' for prefix in prefixes]
