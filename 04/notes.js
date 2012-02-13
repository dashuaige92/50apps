function Note(content, x, y) {
    this.content = content;
    this.x = x;
    this.y = y;
}

function loadNotes() {
    if (typeof(localStorage.notes) == 'undefined') {
        return new Array();
    }
    var notes = JSON.parse(localStorage.notes);
    //var $this = $(this);
    for (var i = 0; i < notes.length; i++) {
        if (!$('div#'+i).length) {
            var $this = $('<div>', {
                'id': i,
                'class': 'note draggable',
                'data-x': notes[i].x,
                'data-y': notes[i].y
            })
            .css({
                position: 'absolute',
                left: notes[i].x + 'px',
                top: notes[i].y + 'px'
            })
            .appendTo('body')
                .draggable({
                    stop: function(e) {
                        var $this = $(this);
                        $this.attr('data-x', $this.position().left);
                        $this.attr('data-y', $this.position().top);
                        saveNotes();
                    }
                })
                .append($('<textarea>', {
                    text: notes[i].content
                }))
                .on('change', function() {
                    var $this = $(this);
                    console.log($this);
                    $this.text($this.attr('value'));
                    saveNotes();
                });;
        }
    };
    return notes;
}

function saveNotes() {
    var notes = new Array();
    $('div.note').each(function() {
        var $this = $(this);
        notes.push(new Note($this.find('textarea').text(), $this.data('x'), $this.data('y')));
    })
    localStorage.notes = JSON.stringify(notes);
}

$(document).ready(function() {
    loadNotes();
    $('html').on('click', function(e) {
        var notes = loadNotes();
        notes.push(new Note('New Note', e.pageX, e.pageY));
        localStorage.notes = JSON.stringify(notes);
        loadNotes();
    });
});
