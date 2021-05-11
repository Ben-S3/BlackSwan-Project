# Author: Hope Church
# Date Created: 3/27/2021
# Date updated: 4/5/2021
# Description: inserts objects into database given by parser
import database_objects as dbo 
import selecter as sel
import Filter as filt

def main():
	name = input("Enter event name: ")
	events = sel.find_events_by_name(name)
	j=0
	for i in events:
		j=j+1
		#temp_tags=sel.find_tag_by_event(i)
		print(j,")",i.name, i.date_start,i.date_end)
	num_event=int(input("Enter event number: "))
	sel_event=events[num_event-1]
	posts=sel.find_post_by_event(sel_event)
	j=0
	isnum=False
	sel_post=""
	while not isnum:
		print("number","title","date","time","description","like_num","comment_num","dislike_num","is_comment","parentid","url","issensitive","language","sharecount")
		for i in posts:
			j=j+1
			print(j,")",i.title,i.date,i.time,i.description[:100],i.like_num,i.comment_num,i.dislike_num,i.is_comment,i.parentid,i.url,i.issensitive,i.language,i.sharecount)
		num_post=input("Enter post number or keywords to filter on: ")
		if num_post.isdigit():
			sel_post=posts[int(num_post)-1]
			isnum=True
		else:
			posts=filt.filterMedia(posts, num_post)
	medias=sel.find_media_by_post(sel_post)
	urls=sel.find_url_by_post(sel_post)
	for i in urls:
		print(i.url)
	
main()
	
	
	
