<?php
/**
 * Plugin Name: KingPo Content Core
 * Description: Core content model, workflow, validation, and WP-CLI operations for KingPo B2B sites.
 * Version: 0.1.0
 * Author: KingPo
 * Text Domain: kingpo-content-core
 */

if (!defined('ABSPATH')) {
    exit;
}

define('KINGPO_CONTENT_CORE_VERSION', '0.1.0');
define('KINGPO_CONTENT_CORE_FILE', __FILE__);
define('KINGPO_CONTENT_CORE_DIR', plugin_dir_path(__FILE__));

require_once KINGPO_CONTENT_CORE_DIR . 'src/Plugin.php';

add_action('plugins_loaded', static function (): void {
    \KingPo\ContentCore\Plugin::instance()->boot();
});
