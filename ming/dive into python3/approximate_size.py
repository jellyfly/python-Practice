def approximate_size(size, a_kilobyte_is_1024_bytes=True):
	if size < 0:
		raise ValueError('number must be non-negative')

	multiple = 1024 if a_kilobyte_is_1024_bytes else 1000
	for suffix in SUFFIXES[multiple]:
		size /= multiple
		if size < multiple:
			return '{0:.1f} {1}'.format(size, suffix)

	raise ValueError('number too large')
