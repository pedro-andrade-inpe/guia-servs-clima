var gulp = require('gulp');
var sass = require('gulp-sass');
var njk_render = require('gulp-nunjucks');
var browserSync = require('browser-sync').create();
var concat = require('gulp-concat');
var minify = require('gulp-minify');
var clean_css = require('gulp-clean-css');
var sourcemaps = require('gulp-sourcemaps');


const { series, parallel } = require('gulp');

// !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
//Verifique os Componentes Bootstrap que não serão usados 
// e       C O M E N T E !!  a linha para retirá-lo do bundle (all.js)
// 
var config = {
    jsConcatFiles: [
        'node_modules/bootstrap/dist/js/bootstrap.min.js',
        'node_modules/bootstrap/js/dist/base-component.js',
        'node_modules/bootstrap/js/dist/alert.js',
        'node_modules/bootstrap/js/dist/button.js',
        'node_modules/bootstrap/js/dist/carousel.js',
        //'node_modules/bootstrap/js/dist/dropdown.js',
        'node_modules/bootstrap/js/dist/collapse.js',
        'node_modules/bootstrap/js/dist/modal.js',
        'node_modules/bootstrap/js/dist/offcanvas.js',
        'node_modules/bootstrap/js/dist/popover.js',
        // 'node_modules/bootstrap/js/dist/scrollspy.js',
        'node_modules/bootstrap/js/dist/tab.js',
        'node_modules/bootstrap/js/dist/toast.js',
        'node_modules/bootstrap/js/dist/tooltip.js',
    ], 
};

function compile_sass(){
    return gulp.src('src/sass/*.scss')
        .pipe(sass().on('error', sass.logError))
        //.pipe(sourcemaps.init()) // Source Maps 
        .pipe(clean_css())
        //.pipe(sourcemaps.write())  // Source Maps 
        .pipe(gulp.dest('dist/css'))
        .pipe(browserSync.stream());
}
function build_bootstrap(){
    // return gulp.src('src/js/*.js')
    //     .pipe(concat('bundle.js'))
    //     .pipe(gulp.dest('dist/js'))
    //     .pipe(minify({ext:{min:'.min.js'}}))
    //     .pipe(gulp.dest('dist/js'))

    return gulp.src(config.jsConcatFiles)
    .pipe(sourcemaps.init())
    .pipe(concat('bootstrap_bundle.js'))
    //.pipe(gulp.dest('src/scripts/js'))
    //.pipe(rename({suffix: '.min'}))
    .pipe(minify({ext:{min:'.min.js'}}))
    .pipe(gulp.dest('dist/js/'))
    //.pipe(reload({stream:true}));
}

function concat_js(){
    return gulp.src('src/js/*.js')
        .pipe(concat('app.js'))
        .pipe(gulp.dest('dist/js'))
        .pipe(minify({ext:{min:'.min.js'}}))
        .pipe(gulp.dest('dist/js'))

    // return gulp.src(config.jsConcatFiles)
    // .pipe(sourcemaps.init())
    // .pipe(concat('all.js'))
    // //.pipe(gulp.dest('src/scripts/js'))
    // //.pipe(rename({suffix: '.min'}))
    // .pipe(minify({ext:{min:'.min.js'}}))
    // .pipe(gulp.dest('dist/js/'))
    // //.pipe(reload({stream:true}));
}

function copy_assets() {
    return gulp.src('node_modules/@fortawesome/fontawesome-free/webfonts/*')
        .pipe(gulp.dest('dist/webfonts/'));
};
function copy_images() {
    return gulp.src('src/images/*')
        .pipe(gulp.dest('dist/images/'));
};

function njk(){
    // compila Nunjucks
    //  **/.html porque queremos os templates também ! 
    //  facilita copia pro projeto django.
    
    return gulp.src('src/njks/**/*.njks')
        .pipe(njk_render.compile())
        .pipe(gulp.dest('dist'))
};

function watch(){
    browserSync.init({
        server: "dist/."
    });
    gulp.watch('src/njks/**/*.njks', njk);
    gulp.watch('src/sass/**/*.scss', compile_sass);
    gulp.watch('src/js/**/*.js', concat_js);
    gulp.watch('src/images/**/*.*', copy_images);

    gulp.watch('src/njks/**/*.njks').on('change', browserSync.reload);
    gulp.watch('src/sass/**/*.scss').on('change', browserSync.reload);
    gulp.watch('src/js/**/*.js').on('change', browserSync.reload);
    gulp.watch('src/images/**/*.*', browserSync.reload);
}


exports.default = series(parallel(compile_sass, build_bootstrap,copy_images , concat_js, njk, copy_assets), watch);
// exports.build = series(clean, parallel(css, javascript));
