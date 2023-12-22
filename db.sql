CREATE TABLE "images" (
  "id" integer PRIMARY KEY,
  "image_url" varchar
);

CREATE TABLE "addresses" (
  "id" integer PRIMARY KEY,
  "address_line_1" varchar,
  "address_line_2" varchar,
  "country" varchar,
  "state" varchar,
  "city" varchar,
  "postal_code" varchar,
  "longitude" decimal,
  "latitude" decimal
);

CREATE TABLE "contact_info" (
  "id" int PRIMARY KEY,
  "user_id" integer,
  "name" varchar,
  "email" varchar(254),
  "phone" varchar,
  "notes" text
);

CREATE TABLE "licenses" (
  "id" int PRIMARY KEY,
  "file" varchar
);

CREATE TABLE "prices" (
  "id" int PRIMARY KEY,
  "amount" decimal,
  "currency" varchar
);

-- CREATE TABLE "users" (
--   "id" integer PRIMARY KEY,
--   "role" varchar,
--   "user_id" int UNIQUE,
--   "profile_image_id" integer
-- );

CREATE TABLE "customers" (
  "id" integer PRIMARY KEY,
  "user_id" integer,
  "address_id" integer
);

CREATE TABLE "agents" (
  "id" integer PRIMARY KEY,
  "user_id" integer,
  "contact_id" integer,
  "license_id" integer,
  "rating" int
);

CREATE TABLE "properties" (
  "id" integer PRIMARY KEY,
  "title" varchar,
  "description" text,
  "type" varchar,
  "price_id" integer,
  "market_value" integer,
  "address_id" integer,
  "bedrooms" integer,
  "bathrooms" integer,
  "area" integer,
  "status" varchar,
  "agent_id" integer,
  "date_listed" timestamp
);

CREATE TABLE "amenities" (
  "id" integer PRIMARY KEY,
  "property_id" integer,
  "name" varchar,
  "description" text,
  "image_id" integer
);

-- CREATE TABLE "contracts" (
--   "id" int PRIMARY KEY,
--   "property_id" integer,
--   "customer_id" integer,
--   "transaction_id" integer,
--   "date" timestamp
-- );

CREATE TABLE "transactions" (
  "id" integer PRIMARY KEY,
  "price_id" integer,
  "date" timestamp
);

CREATE TABLE "reviews" (
  "id" integer PRIMARY KEY,
  "property_id" integer,
  "customer_id" integer,
  "rating" integer,
  "comment" text
);

CREATE TABLE "favorites" (
  "customer_id" integer,
  "property_id" integer
);

CREATE TABLE "blogs" (
  "id" integer PRIMARY KEY,
  "user_id" integer,
  "title" varchar,
  "body" text
);

COMMENT ON COLUMN "properties"."description" IS 'Description of the property';

COMMENT ON COLUMN "properties"."date_listed" IS 'Date when the property was listed';

-- ALTER TABLE "blogs" ADD FOREIGN KEY ("user_id") REFERENCES "users" ("id");

-- ALTER TABLE "customers" ADD FOREIGN KEY ("user_id") REFERENCES "users" ("id");

ALTER TABLE "customers" ADD FOREIGN KEY ("address_id") REFERENCES "addresses" ("id");

-- ALTER TABLE "agents" ADD FOREIGN KEY ("user_id") REFERENCES "users" ("id");

ALTER TABLE "agents" ADD FOREIGN KEY ("contact_id") REFERENCES "contact_info" ("id");

ALTER TABLE "agents" ADD FOREIGN KEY ("license_id") REFERENCES "licenses" ("id");

ALTER TABLE "properties" ADD FOREIGN KEY ("price_id") REFERENCES "prices" ("id");

ALTER TABLE "properties" ADD FOREIGN KEY ("market_value") REFERENCES "prices" ("id");

ALTER TABLE "properties" ADD FOREIGN KEY ("address_id") REFERENCES "addresses" ("id");

ALTER TABLE "amenities" ADD FOREIGN KEY ("property_id") REFERENCES "properties" ("id");


-- ALTER TABLE "images" ADD FOREIGN KEY ("id") REFERENCES "users" ("profile_image_id");

-- ALTER TABLE "contracts" ADD FOREIGN KEY ("property_id") REFERENCES "properties" ("id");

-- ALTER TABLE "contracts" ADD FOREIGN KEY ("customer_id") REFERENCES "customers" ("id");

-- ALTER TABLE "transactions" ADD FOREIGN KEY ("id") REFERENCES "contracts" ("transaction_id");

ALTER TABLE "transactions" ADD FOREIGN KEY ("price_id") REFERENCES "prices" ("id");

ALTER TABLE "properties" ADD FOREIGN KEY ("agent_id") REFERENCES "agents" ("id");

ALTER TABLE "reviews" ADD FOREIGN KEY ("property_id") REFERENCES "properties" ("id");

ALTER TABLE "reviews" ADD FOREIGN KEY ("customer_id") REFERENCES "customers" ("id");

ALTER TABLE "favorites" ADD FOREIGN KEY ("customer_id") REFERENCES "customers" ("id");

ALTER TABLE "favorites" ADD FOREIGN KEY ("property_id") REFERENCES "properties" ("id");

-- ALTER TABLE "contact_info" ADD FOREIGN KEY ("users_id") REFERENCES "users" ("id");

-- ALTER TABLE "users" ADD FOREIGN KEY ("user_id") REFERENCES "auth_user" ("id");
