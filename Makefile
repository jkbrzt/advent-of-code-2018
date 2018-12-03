run-all:
	for py in day??.py; do echo; echo $$py; python3 $$py ; done
