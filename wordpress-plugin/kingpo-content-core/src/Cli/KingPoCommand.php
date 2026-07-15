<?php

namespace KingPo\ContentCore\Cli;

if (!defined('ABSPATH')) {
    exit;
}

final class KingPoCommand
{
    public function site($args, $assoc_args): void
    {
        \WP_CLI::success(json_encode([
            'wp_version' => get_bloginfo('version'),
            'site_url' => site_url(),
            'active_theme' => wp_get_theme()->get('Name'),
        ]));
    }

    public function release($args, $assoc_args): void
    {
        \WP_CLI::success(json_encode([
            'status' => 'stub',
            'message' => 'Release checks will be implemented in a later milestone.',
        ]));
    }

    public function product($args, $assoc_args): void
    {
        \WP_CLI::success(json_encode([
            'status' => 'stub',
            'message' => 'Product validation/import/export commands will be implemented in a later milestone.',
        ]));
    }
}
