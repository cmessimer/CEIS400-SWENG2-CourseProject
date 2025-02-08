# Database Schema

CREATE DATABASE EquipmentCheckoutDB;
USE EquipmentCheckoutDB;

CREATE TABLE Users (
    UserID INT IDENTITY(1,1) PRIMARY KEY,
    Name NVARCHAR(100),
    Role NVARCHAR(50),
    Email NVARCHAR(100),
    PasswordHash NVARCHAR(255)
);

CREATE TABLE Equipment (
    EquipmentID INT IDENTITY(1,1) PRIMARY KEY,
    Name NVARCHAR(100),
    Status NVARCHAR(50),
    Location NVARCHAR(100)
);

CREATE TABLE CheckoutRecords (
    RecordID INT IDENTITY(1,1) PRIMARY KEY,
    UserID INT FOREIGN KEY REFERENCES Users(UserID),
    EquipmentID INT FOREIGN KEY REFERENCES Equipment(EquipmentID),
    CheckoutDate DATETIME DEFAULT GETDATE(),
    ReturnDate DATETIME NULL
);
