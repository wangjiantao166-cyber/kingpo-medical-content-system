# Plugin and Theme Contract

The base plugin owns content types, taxonomies, roles, workflow states, validation, REST, WP-CLI, audit logs, import/export, and release checks.

The base theme owns layout, templates, patterns, theme.json, front-end styles, and display behavior.

Dynamic data blocks should be provided by the plugin. The theme must not own product facts or approval status.
