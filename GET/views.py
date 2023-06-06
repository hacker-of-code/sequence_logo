from django.shortcuts import render
import logomaker

from django.http import HttpResponse

def get_sequence_logo(request):

    sequence = request.session.get("sequence", "")

    if not create_logo(sequence):
        pass

    return render(request, 'get_sequence_logo.html')

def create_logo(sequence):
    sequence = sequence.upper()
    sequence = sequence.split('\r\n')

    matrix = logomaker.alignment_to_matrix(sequence, to_type='information', pseudocount=0.0)

    # create Logo object
    ww_logo = logomaker.Logo(matrix,
                            font_name='Arial',
                            color_scheme='chemistry',
                            vpad=.01,
                            width=.8)

    # style using Logo methods
    ww_logo.style_xticks(anchor=0, spacing=1, rotation=90)
    # ww_logo.highlight_position(p=4, color='gold', alpha=.5)

    # style using Axes methods
    ww_logo.ax.set_ylabel('information (bits)')
    ww_logo.ax.set_xlim([-1, len(matrix)])

    # save figure
    ww_logo.fig.savefig('GET/templates/static/logo.png', dpi=100, transparent=False)
    return True
