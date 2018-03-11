create table Users(
	userID INTEGER,
	email CHAR(40),
    password char(40),
    points INTEGER,
    PRIMARY KEY (userID),
    UNIQUE KEY (email)
	);
    
create table Hacks(
	hackID INTEGER,
	userID INTEGER,
	content CHAR(240),
    tag CHAR(40),
    PRIMARY KEY (hackID),
    FOREIGN KEY (userID) REFERENCES Users(userID)
    );

create table Likes(
	userID INTEGER,
    hackID INTEGER,
    PRIMARY KEY (userID, hackID),
    FOREIGN KEY (userID) references Users(userID),
    FOREIGN KEY (hackID) references Hacks(hackID)
    );
    
create table Tags(
	name CHAR(40),
    primary key (name)
    );

create table HacksTags(
	name CHAR(40),
    hackID INTEGER,
    PRIMARY KEY (name, hackID),
    FOREIGN KEY (name) REFERENCES Tags(name),
    FOREIGN KEY (hackID) REFERENCES Hacks(hackID)
    );
    
