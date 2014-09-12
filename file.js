define(function (require) {
    var BB = require('backbone'),
        $ = require('jquery'),
        _ = require('underscore'),
        Settings = require('settings'),
        template = require('hgn!widgets/templates/post_approval'),
        PostApprovalModel = require('widgets/models/post_approval'),
        Informer = require('widgets/views/informer'),
        require('libs/jquery/plugins/jquery.mobile.custom');

    return BB.View.extend({
        events: {
            'click .close-icon': 'remove'
            , 'click .approve': 'approve'
        }
        , initialize: function() {
            this.model = new PostApprovalModel({site_id: Settings.site.id, post_id: this.options.post_id});
            this.approvePost = function (siteId, draftId) {
                return new(BB.Model.extend({
                    url: '/core/community/approval/' + siteId + '/' + draftId + '/'
                }))();
            };
            _.bindAll(this, '_render');
            this.model.fetch({
                success: this._render
            });
        }
        , _render: function() {
            var template_data = _.extend({}, this.model.toJSON(), Settings.site.owner_data);
            this.$el.html(template(template_data));
            this.$('#rules-agreement').removeAttr('disabled');
            return this;
        }
        , isAgree: function () {
            return this.$('#rules-agreement').attr('checked') || false;
        }
        , approve: function (evnt) {
            var view = this;
            evnt && evnt.preventDefault();
            if (!this.isAgree()) {
                this.errorInform('Please confirm that you agree to the rules and conditions by checking the box above');
                return;
            }
            this.approvePost(this.model.get('site_id'), this.model.get('id')).save({}, {
                success: function (data) {
                    var redirect = data.get('redirect');
                    if (redirect) {
                        window.location = redirect;
                    } else {
                        view.errorInform('Sorry an error occured');
                    }
                },
                error: function (model, response) {
                    if (response.status === 403) {
                        view.errorInform('Forbidden');
                    } else {
                        view.errorInform('Sorry an error occured');
                    }
                }
            });
        }
        , errorInform: function (message) {
            (new Informer({
                message: message || 'Error has occured'
                , type: 'error'
                , headline: 'Oops'
                , controls: [{name: 'OK', callback: $.noop}]
            })).render();

        }
    });
});
