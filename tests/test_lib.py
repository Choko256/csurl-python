from csurl import CSUrl

def test_shorten():
	result = CSUrl.shorten('https://www.digitalocean.com/community/tutorials/how-to-secure-nginx-with-let-s-encrypt-on-ubuntu-16-04')
	assert result['short'] == 'WQ0ON'

def test_get():
	result = CSUrl.get('WQ0ON')
	assert result['target'] == 'https://www.digitalocean.com/community/tutorials/how-to-secure-nginx-with-let-s-encrypt-on-ubuntu-16-04'

