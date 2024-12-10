-- Keep a log of any SQL queries you execute as you solve the mystery.

-- Find the description of the crime scene
SELECT description FROM crime_scene_reports WHERE month = 7 AND day = 28 AND street = 'Humphrey Street';

-- Find the interviews for the day the crime happended
SELECT transcript FROM interviews WHERE month = 7 AND day = 28;

-- Find the car which left the parking lot within 10 minutes (I checked from minute 16-25)
SELECT activity, license_plate FROM bakery_security_logs WHERE month = 7 AND day = 28 AND hour = 10 AND minute = 16-25;

-- Find the thiefs account numbers
SELECT account_number, transaction_type, amount FROM atm_transactions WHERE month = 7 AND day = 28 AND atm_location = 'Leggett Street';
