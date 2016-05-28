{
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
      'cflags' : [ '-std=c++14', '-stdlib=libc++' ],
      'conditions': [
          [ 'OS!="win"', {
            'cflags+': [ '-std=c++14' ],
            'cflags_c+': [ '-std=c++14' ],
            'cflags_cc+': [ '-std=c++14' ],
          }],
          [ 'OS=="mac"', {
            'xcode_settings': {
              'OTHER_CPLUSPLUSFLAGS' : [ '-std=c++14', '-stdlib=libc++' ],
              'MACOSX_DEPLOYMENT_TARGET': '10.7'
            },
          }],
        ],
    },
    {
      'target_name': 'test',
      'type': 'executable',
      'dependencies': [
        'nangraph',
        "<!(node -e \"console.log(require.resolve('catch.cc/gyp/package.gyp') + ':*')\")"
      ],
      'sources': [
        '../test/main.cc'
      ],
      'cflags' : [ '-std=c++14', '-stdlib=libc++' ],
      'conditions': [
          [ 'OS!="win"', {
            'cflags+': [ '-std=c++14' ],
            'cflags_c+': [ '-std=c++14' ],
            'cflags_cc+': [ '-std=c++14' ],
          }],
          [ 'OS=="mac"', {
            'xcode_settings': {
              'OTHER_CPLUSPLUSFLAGS' : [ '-std=c++14', '-stdlib=libc++' ],
              "OTHER_LDFLAGS": [ "-stdlib=libc++" ],
              'MACOSX_DEPLOYMENT_TARGET': '10.7',
              'GCC_ENABLE_CPP_EXCEPTIONS': 'YES',        # override -fno-exceptions
            },
          }],
        ],
    }
  ]
}
