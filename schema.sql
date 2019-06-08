drop table if exists posts;
	create table posts (
		TSTAMP DATETIME NOT NULL DEFAULT(GetDate()),
		NAME text not null,
		CONTENT text not null
);
