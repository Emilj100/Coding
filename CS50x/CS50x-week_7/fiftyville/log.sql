-- Keep a log of any SQL queries you execute as you solve the mystery.

-- Find the description of the crime scene
SELECT description FROM crime_scene_reports WHERE month = 7 AND day = 28 AND street = 'Humphrey Street';

-- Find the interviews for the day the crime happended
SELECT transcript FROM interviews WHERE month = 7 AND day = 28;

-- Find the car which left the parking lot within 10 minutes (I checked from minute 16-25)
SELECT activity, license_plate FROM bakery_security_logs WHERE month = 7 AND day = 28 AND hour = 10 AND minute = 16-25;

-- Find the thiefs account number
SELECT account_number, transaction_type, amount FROM atm_transactions WHERE month = 7 AND day = 28 AND atm_location = 'Leggett Street';

-- Check the information on the account number (I checked multiple account numbers)
SELECT person_id, creation_year FROM bank_accounts WHERE account_number = 25506511;

-- Check phone calls on the day under a minute in duration
SELECT caller, receiver, duration FROM phone_calls WHERE month = 7 AND day = 28 AND duration <= 60;

-- Check the information on Fiftyville airport
SELECT id, abbreviation, full_name FROM airports WHERE city = 'Fiftyville';

-- Check the flights the day after the crime
select id, destination_airport_id, hour, minute FROM flights WHERE origin_airport_id = 8 AND month = 7 AND day = 29;

-- Check the passengers information on the earliest flight the day after the crime
SELECT passport_number, seat FROM passengers WHERE flight_id = 36;

-- Check the phone_number, passport_number and license_plate to see if they match(I checked all passport numbers and tried to match them with license_plate and phone_number)
SELECT id, name, phone_number, passport_number, license_plate FROM people WHERE passport_number = 1695452385;

-- Check if the person_id from the people table matches any bank accounts (I checked all the person_id's)
SELECT account_number, person_id, creation_year FROM bank_accounts WHERE person_id = 449774;

-- Checked if the different suspects made a transaction on the given day the crime happend (I checked all the account numbers)
SELECT id, account_number, transaction_type, amount FROM atm_transactions WHERE month = 7 AND day = 28 AND account_number = 49610011;

-- Checked the destination airport ID to see where the thief went
SELECT id, full_name, city FROM airports WHERE id = 4;

-- Checked who my suspect talked with on the given day
SELECT id, caller, receiver, duration FROM phone_calls WHERE month = 7 AND day = 28 AND duration <= 60 AND caller = '(367) 555-5533';

-- Checked the name of the person my suspect talked with
SELECT name, phone_number FROM people WHERE phone_number = '(375) 555-8161';





