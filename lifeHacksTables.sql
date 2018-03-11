create table Users(
	userID INTEGER,
	email CHAR(40),
    password char(40),
    points INTEGER,
    PRIMARY KEY (email),
    UNIQUE KEY (email)
	);
    
create table Hacks(
	hackID INTEGER,
	content CHAR(240),
    userID INTEGER,
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
    
    