from config import huey
import subprocess


@huey.task()
def render_to_png(url, file_id, sync):
    print('-- [render_to_png] render url "%s" to png --' % url)

    args = ['corylus/vendors/phantomjs/phantomjs',
            'corylus/vendors/phantomjs/render.js',
            'url=%s' % url,
            'name=%s' % file_id,
            ]
    result = subprocess.check_output(args)
    print('-- [render_to_png] result', result)
    success = 'success' in result
    return {
        'file_id': file_id,
        'sync': sync,
        'success': success,
    }
