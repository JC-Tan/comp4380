CREATE TABLE daily_passenger_activity (
	schedule_period_name		varchar(20),
	schedule_period_start_date	timestamp,
	schedule_period_end_date	timestamp,
	stop_number					integer,
	route_number				integer,
	route_name					varchar(255),
	day_type					varchar(10),
	time_period					varchar(10),
	average_boardings			decimal,
	average_alightings			decimal,
	location					varchar(100),
	PRIMARY KEY(
		schedule_period_name,
		schedule_period_start_date,
		schedule_period_end_date,
		stop_number,
		route_number,
		day_type,
		time_period
	)
);

--Pass-Up ID,Pass-Up Type,Time,Route Number,Route Name,Route Destination,Location
CREATE TABLE transit_pass_up (
	pass_up_id					integer PRIMARY KEY NOT NULL,
	pass_up_type				varchar(50),
	pass_up_time				timestamp,
	route_number				integer,
	route_name					varchar(255),
	route_destination			varchar(255),
	location					varchar(100),
);

COPY public.daily_passenger_activity FROM '{PATH_TO}\dailyPassengerActivity.txt' (FORMAT CSV, DELIMITER(','));
COPY public.transit_pass_up FROM '{PATH_TO}\transitPassUp.txt' (FORMAT CSV, DELIMITER(','));
