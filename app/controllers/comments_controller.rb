class CommentsController < ApplicationController
  def create
    @food = Food.find(params[:food_id])

    @comment = @food.comments.create(comment_params)

    redirect_to food_path(@food)
  end

  private
    def comment_params
      params.require(:comment).permit(:user,:title,:body,:food)
    end
end
