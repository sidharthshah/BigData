#!/usr/bin/python
import sys
from collections import Counter
previous_user_id = ""
queries = []
clicked_domains = []

def parse_record(record):
	user_id = "" 
	q = "" 
	ts = "" 
	click_rank = ""
	clicked_domain = ""

	tokens = record.split("\t")
	user_id = tokens[0]
	q = tokens[1]
	ts = tokens[2]

	if len(tokens) > 3:
		click_rank = tokens[3]

	if len(tokens) > 4:
		clicked_domain = tokens[4]

	return user_id, q, ts, click_rank, clicked_domain

def emmit_ts_qs(ts, q):
	print "%s\t%s" % (ts, q)

def emmit_ts_clicks(ts, clicked_domain):
	print "%s\t%s" % (ts, clicked_domain)

def emmit_user_query_count(user_id, q, ts, click_rank, clicked_domain, gen_click_counts=False):
	global previous_user_id, queries, clicked_domains
	user_id, q, ts, click_rank, clicked_domain = parse_record(record)
	if user_id != previous_user_id:
		previous_user_id = user_id
		
		query_counter = Counter(queries)
		if not gen_click_counts:
			for k,v in query_counter.items():
				print "%s\t%s\t%s" % (user_id, k, v)
		queries = []

		clicked_domains_counter = Counter(clicked_domains)
		if gen_click_counts:
			for k,v in clicked_domains_counter.items():
				print "%s\t%s\t%s" % (user_id, k, v)		
		clicked_domains = []

	queries.append(q)

	if clicked_domain.strip() != "":
		clicked_domains.append(clicked_domain)

def emmit_query(q):
	print "%s\t1" % (q)

for record in sys.stdin:
	record = record.strip()
	user_id, q, ts, click_rank, clicked_domain = parse_record(record)

	if len(sys.argv) > 1 and sys.argv[1] == 'ts_qs_pair':
		emmit_ts_qs(ts, q)

	if len(sys.argv) > 1 and sys.argv[1] == 'ts_clicks_pair':
		if click_rank.strip() != "":
			emmit_ts_clicks(ts, clicked_domain)

	if len(sys.argv) > 1 and sys.argv[1] == 'user_query_counts':
		emmit_user_query_count(user_id, q, ts, click_rank, clicked_domain)

	if len(sys.argv) > 1 and sys.argv[1] == 'user_click_counts':
		emmit_user_query_count(user_id, q, ts, click_rank, clicked_domain, True)

	if len(sys.argv) > 1 and sys.argv[1] == 'query_counts':
		emmit_query(q)
