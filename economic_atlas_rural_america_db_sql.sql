-- Exported from QuickDBD: https://www.quickdatabasediagrams.com/
-- Link to schema: https://app.quickdatabasediagrams.com/#/d/T7GRz5
-- NOTE! If you have used non-SQL datatypes in your design, you will have to change these here.


CREATE TABLE "jobs" (
    "fips" VARCHAR(05)   NOT NULL,
    "state" VARCHAR(2)   NOT NULL,
    "county" VARCHAR(40)   NOT NULL,
    "pctemp_agriculture" DECIMAL   NOT NULL,
    "pctemp_mining" DECIMAL   NOT NULL,
    "pctemp_construction" DECIMAL   NOT NULL,
    "pctemp_manufacturing" DECIMAL   NOT NULL,
    "pctemp_trade" DECIMAL   NOT NULL,
    "pctemp_trans" DECIMAL   NOT NULL,
    "pctemp_information" DECIMAL   NOT NULL,
    "pctemp_fire" DECIMAL   NOT NULL,
    "pctemp_services" DECIMAL   NOT NULL,
    "pctemp_government" DECIMAL   NOT NULL,
    "num_civ_employed" DECIMAL  NOT NULL,
    "last_update" timestamp  DEFAULT Localtimestamp NOT NULL,
    CONSTRAINT "pk_jobs" PRIMARY KEY (
        "fips"
     )
);

CREATE TABLE "income" (
    "fips" VARCHAR(05)   NOT NULL,
    "state" VARCHAR(2)   NOT NULL,
    "county" VARCHAR(40)   NOT NULL,
    "median_hh_inc_acs" DECIMAL   NOT NULL,
    "percapita_inc" DECIMAL   NOT NULL,
    "poverty_rate_0_17_acs" DECIMAL   NOT NULL,
    "poverty_rate_acs" DECIMAL   NOT NULL,
    "deep_pov_all" DECIMAL   NOT NULL,
    "deep_pov_children" DECIMAL   NOT NULL,
    "num_allinpov_acs" DECIMAL   NOT NULL,
    "pct_pov_0_17" DECIMAL   NOT NULL,
    "pov_0_17" DECIMAL   NOT NULL,
    "med_hh_inc" DECIMAL   NOT NULL,
    "pov_all" DECIMAL   NOT NULL,
    "pct_pov_all" DECIMAL   NOT NULL,
    "num_in_pov_0_17_acs" DECIMAL   NOT NULL,
    "last_update" timestamp  DEFAULT Localtimestamp NOT NULL,
    CONSTRAINT "pk_income" PRIMARY KEY (
        "fips"
     )
);

CREATE TABLE "unemployment" (
    "fips" VARCHAR(05)   NOT NULL,
    "year" VARCHAR(04)   NOT NULL,
    "unemp_rate" DECIMAL   NOT NULL,
    "num_unemployed" DECIMAL   NOT NULL,
    "last_update" timestamp  DEFAULT Localtimestamp NOT NULL,
    CONSTRAINT "pk_unemloyment" PRIMARY KEY (
        "fips"
     )
);

CREATE TABLE "employment" (
    "fips" VARCHAR(05)   NOT NULL,
    "year" VARCHAR(04)   NOT NULL,
    "num_civ_labor_force" DECIMAL  NOT NULL,
    "num_employed" DECIMAL   NOT NULL,
    "last_update" timestamp  DEFAULT Localtimestamp NOT NULL,
    CONSTRAINT "pk_employment" PRIMARY KEY (
        "fips"
     )
);

ALTER TABLE "unemployment" ADD CONSTRAINT "fk_unemloyment_fips" FOREIGN KEY("fips")
REFERENCES "jobs" ("fips");

ALTER TABLE "employment" ADD CONSTRAINT "fk_employment_fips" FOREIGN KEY("fips")
REFERENCES "jobs" ("fips");

