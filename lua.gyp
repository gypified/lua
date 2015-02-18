# vim: ft=python sw=2 ts=2
# pylint: disable=W0104
{
  'conditions': [
    ['OS=="linux"', {
      'target_defaults': {
        'defines': [ 'LUA_USE_LINUX' ],
      },
    }],
    ['OS=="mac"', {
      'target_defaults': {
        'defines': [ 'LUA_USE_MACOSX' ],
      },
    }],
    ['OS=="solaris"', {
      'target_defaults': {
        'defines': [ 'LUA_USE_POSIX', 'LUA_USE_DLOPEN' ],
      },
    }],
  ],
  'targets': [
    {
      'target_name': 'liblua',
      'type': 'static_library',
      'direct_dependent_settings': {
        'include_dirs': [ './src' ],
      },
      'sources': [
        'src/lapi.c',
        'src/lcode.c',
        'src/lctype.c',
        'src/ldebug.c',
        'src/ldo.c',
        'src/ldump.c',
        'src/lfunc.c',
        'src/lgc.c',
        'src/llex.c',
        'src/lmem.c',
        'src/lobject.c',
        'src/lopcodes.c',
        'src/lparser.c',
        'src/lstate.c',
        'src/lstring.c',
        'src/ltable.c',
        'src/ltm.c',
        'src/lundump.c',
        'src/lvm.c',
        'src/lzio.c',

        'src/lauxlib.c',
        'src/lbaselib.c',
        'src/lbitlib.c',
        'src/lcorolib.c',
        'src/ldblib.c',
        'src/liolib.c',
        'src/lmathlib.c',
        'src/loslib.c',
        'src/lstrlib.c',
        'src/ltablib.c',
        'src/lutf8lib.c',
        'src/loadlib.c',
        'src/linit.c',
      ],
      'link_settings': {
        'libraries': [ '-lm' ],
      },
      'conditions': [
        ['OS=="linux"', {
          'cflags': [ '-Wl,-E' ],
          'link_settings': {
            'libraries': [ '-ldl' ],
          },
        }],
        ['OS=="mac"', {
          'link_settings': {
            'libraries': [ '-ldl' ],
          },
        }],
        ['OS=="solaris"', {
          'link_settings': {
            'libraries': [ '-ldl' ],
          },
          'all_dependent_settings': {
            'defines': [ '_REENTRANT' ],
          },
        }],
      ],
    },
    {
      'target_name': 'lua',
      'type': 'executable',
      'dependencies': [ 'liblua' ],
      'sources': [ 'src/lua.c' ],
      'conditions': [
        ['OS=="linux"', {
          'libraries': [ '-lreadline' ],
        }],
        ['OS=="mac"', {
          'libraries': [ '-lreadline' ],
        }],
      ],
    },
    {
      'target_name': 'luac',
      'type': 'executable',
      'dependencies': [ 'liblua' ],
      'sources': [ 'src/luac.c' ],
    },
  ],
}
