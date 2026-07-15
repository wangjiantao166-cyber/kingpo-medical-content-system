<?php

namespace KingPo\ContentCore;

if (!defined('ABSPATH')) {
    exit;
}

final class Plugin
{
    private static ?self $instance = null;

    public static function instance(): self
    {
        if (self::$instance === null) {
            self::$instance = new self();
        }
        return self::$instance;
    }

    public function boot(): void
    {
        add_action('init', [$this, 'register_post_types']);
        add_action('init', [$this, 'register_taxonomies']);
        add_action('init', [$this, 'register_statuses']);
        add_action('init', [$this, 'register_roles']);
        add_action('admin_notices', [$this, 'acf_notice']);

        if (defined('WP_CLI') && WP_CLI) {
            require_once KINGPO_CONTENT_CORE_DIR . 'src/Cli/KingPoCommand.php';
            \WP_CLI::add_command('kingpo', \KingPo\ContentCore\Cli\KingPoCommand::class);
        }
    }

    public function register_post_types(): void
    {
        $types = [
            'product' => 'Products',
            'standard' => 'Standards',
            'standard_mapping' => 'Standard Mappings',
            'test_method' => 'Test Methods',
            'solution' => 'Solutions',
            'resource' => 'Resources',
            'case' => 'Cases',
        ];

        foreach ($types as $type => $label) {
            register_post_type($type, [
                'label' => $label,
                'public' => in_array($type, ['product', 'standard', 'test_method', 'solution', 'resource', 'case'], true),
                'show_in_rest' => true,
                'supports' => ['title', 'editor', 'excerpt', 'thumbnail', 'revisions'],
                'has_archive' => $type !== 'standard_mapping',
                'rewrite' => ['slug' => str_replace('_', '-', $type)],
            ]);
        }
    }

    public function register_taxonomies(): void
    {
        $taxonomies = [
            'product_domain' => ['product'],
            'application_industry' => ['product', 'solution', 'resource'],
            'test_object' => ['product', 'test_method'],
            'test_method_type' => ['product', 'test_method'],
            'standard_organization' => ['standard', 'standard_mapping'],
            'resource_type' => ['resource'],
            'asset_type' => ['attachment'],
        ];

        foreach ($taxonomies as $taxonomy => $objects) {
            register_taxonomy($taxonomy, $objects, [
                'label' => ucwords(str_replace('_', ' ', $taxonomy)),
                'public' => !in_array($taxonomy, ['asset_type'], true),
                'show_in_rest' => true,
                'hierarchical' => in_array($taxonomy, ['product_domain', 'standard_organization', 'resource_type'], true),
                'rewrite' => ['slug' => str_replace('_', '-', $taxonomy)],
            ]);
        }
    }

    public function register_statuses(): void
    {
        foreach (['source_pending', 'technical_review', 'standards_review', 'seo_review', 'ready_for_publish', 'retired', 'blocked'] as $status) {
            register_post_status($status, [
                'label' => ucwords(str_replace('_', ' ', $status)),
                'public' => false,
                'internal' => false,
                'show_in_admin_status_list' => true,
                'show_in_admin_all_list' => true,
            ]);
        }
    }

    public function register_roles(): void
    {
        $roles = [
            'kp_product_editor' => 'KingPo Product Editor',
            'kp_engineering_reviewer' => 'KingPo Engineering Reviewer',
            'kp_standards_reviewer' => 'KingPo Standards Reviewer',
            'kp_seo_reviewer' => 'KingPo SEO Reviewer',
            'kp_asset_reviewer' => 'KingPo Asset Reviewer',
            'kp_publisher' => 'KingPo Publisher',
            'kp_site_operator' => 'KingPo Site Operator',
        ];

        foreach ($roles as $role => $label) {
            if (!get_role($role)) {
                add_role($role, $label, ['read' => true, 'upload_files' => true]);
            }
        }
    }

    public function acf_notice(): void
    {
        if (!is_admin() || function_exists('acf_add_local_field_group')) {
            return;
        }
        echo '<div class="notice notice-warning"><p>KingPo Content Core: ACF Pro is recommended for structured field groups. Native meta fallbacks are not implemented yet.</p></div>';
    }
}
