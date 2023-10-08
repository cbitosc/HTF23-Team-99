// search.js
$(document).ready(function () {
    $('#search-input').on('input', function () {
        const query = $(this).val();
        if (query.trim().length === 0) {
            $('#search-results').empty();
        } else {
            $.ajax({
                type: 'GET',
                url: '/search/',
                data: {
                    'query': query
                },
                success: function (data) {
                    const resultsContainer = $('#search-results');
                    resultsContainer.empty();

                    if (data.results.length > 0) {
                        data.results.forEach(function (result) {
                            const item = $('<div>').text(result.name);
                            resultsContainer.append(item);
                        });
                    } else {
                        resultsContainer.html('<p>No results found.</p>');
                    }
                }
            });
        }
    });
});
