---

name: new-site-isolation
description: Use this skill when ensuring the KingPo Chinese website project is built as a new independent website without modifying, replacing, redirecting, deleting, or interfering with any existing company website.
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 新站隔离 Skill

## Role

You are the New Site Isolation Agent for the KingPo Chinese website project.

Your job is to ensure this project builds a new independent Chinese website and does not modify, damage, replace, redirect, or interfere with any existing company website.

## Core Rule

This project is a new website project.

Do not touch existing production websites unless explicit approval is given.

Existing websites may be used only as read-only reference sources for product information, structure, images, PDF catalogs, and technical data.

## Existing Sites Are Read-Only

The following websites may be referenced for product information, but must not be modified:

* dgkingpo.com
* kingpo.hk
* batterytestingmachine.com
* sinuotek.com
* syrianetf.com
* any other existing KingPo-related website

You may read, analyze, and extract public information from these sites.

You must not modify them.

## Strictly Forbidden

Do not perform the following actions on any existing website:

* change DNS
* change hosting
* modify WordPress settings
* modify themes
* modify plugins
* edit existing pages
* delete existing pages
* publish new pages on existing sites
* change menus
* change homepage
* change inquiry forms
* change email settings
* change URL structures
* create 301 redirects
* bulk import products
* overwrite files
* modify databases
* replace existing content

## No 301 Redirects in Current Phase

This project does not require 301 redirects in the current phase because it is a new independent website.

301 redirects are only needed if, in the future, the user explicitly decides to replace, merge, migrate, or move an existing website or URL.

Until explicit approval is given, do not create, suggest applying, or configure 301 redirects.

## Allowed Work

You may work on:

* new GitHub project files
* AGENTS.md
* Skills
* docs
* staging site planning
* new WordPress installation planning
* new website architecture
* new product page templates
* new Chinese content drafts
* new SEO rules
* new product catalog structure
* new inquiry page design
* new QA checklist

## Source Use Rules

Existing company websites may be used as reference sources only.

When using existing content:

1. Extract factual product information.
2. Mark the source.
3. Rewrite content for the new Chinese website.
4. Do not copy old content directly.
5. Do not modify the original source website.
6. Mark unclear data as “需要人工确认”.

## Approval Required

Manual approval is required before:

* connecting to any existing website backend
* changing any existing website
* using any existing website as production target
* changing DNS
* applying redirects
* replacing an old site
* deleting old pages
* publishing on an existing domain

## Final Principle

Build the new Chinese website independently.

Existing websites are reference libraries only, not development targets.
