{
    "targets": [
        {
            "target_name": "pebliss",
            "cflags!": [ '-fno-exceptions' ],
            "cflags_cc!": [ '-fno-exceptions' ],
            "include_dirs" : [
                "<!(node -e \"require('nan')\")"
            ],
            'conditions': [
                ['OS=="mac"', {
                    'xcode_settings': {
                        'GCC_ENABLE_CPP_EXCEPTIONS': 'YES'
                    }
                }],
            ],
            "sources": [
                "src/libpebliss/pe_lib/entropy.cpp",
                "src/libpebliss/pe_lib/file_version_info.cpp",
                "src/libpebliss/pe_lib/message_table.cpp",
                "src/libpebliss/pe_lib/pe_base.cpp",
                "src/libpebliss/pe_lib/pe_bound_import.cpp",
                "src/libpebliss/pe_lib/pe_checksum.cpp",
                "src/libpebliss/pe_lib/pe_debug.cpp",
                "src/libpebliss/pe_lib/pe_directory.cpp",
                "src/libpebliss/pe_lib/pe_dotnet.cpp",
                "src/libpebliss/pe_lib/pe_exception.cpp",
                "src/libpebliss/pe_lib/pe_exception_directory.cpp",
                "src/libpebliss/pe_lib/pe_exports.cpp",
                "src/libpebliss/pe_lib/pe_factory.cpp",
                "src/libpebliss/pe_lib/pe_imports.cpp",
                "src/libpebliss/pe_lib/pe_load_config.cpp",
                "src/libpebliss/pe_lib/pe_properties.cpp",
                "src/libpebliss/pe_lib/pe_properties_generic.cpp",
                "src/libpebliss/pe_lib/pe_rebuilder.cpp",
                "src/libpebliss/pe_lib/pe_relocations.cpp",
                "src/libpebliss/pe_lib/pe_resource_manager.cpp",
                "src/libpebliss/pe_lib/pe_resource_viewer.cpp",
                "src/libpebliss/pe_lib/pe_resources.cpp",
                "src/libpebliss/pe_lib/pe_rich_data.cpp",
                "src/libpebliss/pe_lib/pe_section.cpp",
                "src/libpebliss/pe_lib/pe_tls.cpp",
                "src/libpebliss/pe_lib/resource_bitmap_reader.cpp",
                "src/libpebliss/pe_lib/resource_bitmap_writer.cpp",
                "src/libpebliss/pe_lib/resource_cursor_icon_reader.cpp",
                "src/libpebliss/pe_lib/resource_cursor_icon_writer.cpp",
                "src/libpebliss/pe_lib/resource_data_info.cpp",
                "src/libpebliss/pe_lib/resource_message_list_reader.cpp",
                "src/libpebliss/pe_lib/resource_string_table_reader.cpp",
                "src/libpebliss/pe_lib/resource_version_info_reader.cpp",
                "src/libpebliss/pe_lib/resource_version_info_writer.cpp",
                "src/libpebliss/pe_lib/utils.cpp",
                "src/libpebliss/pe_lib/version_info_editor.cpp",
                "src/libpebliss/pe_lib/version_info_viewer.cpp",

                "src/main.cpp",
            ],
        }
    ]
}

