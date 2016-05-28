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
      'direct_dependent_settings': {
        'include_dirs': [
          '../include'
        ],
      },
    },
  ]
}
