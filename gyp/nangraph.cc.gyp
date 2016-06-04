{
  'includes': [
    './common.gypi'
  ],
  'targets': [{
      'target_name': 'nangraph',
      'type': 'static_library',
      'sources': [
        '../src/graph.cc',
      ],
      'include_dirs': [
          '../include'
      ],
      'all_dependent_settings': {
        'include_dirs': [
          '../include'
        ],
      },
    },
  ]
}
