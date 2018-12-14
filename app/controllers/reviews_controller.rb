class ReviewsController < ApplicationController
  def create
    @food = Food.find(params[:food_id])

    @review = @food.reviews.create(review_params)

    redirect_to food_path(@food)
  end

  private
    def review_params
      params.require(:review).permit(:reviewer, :review, :rating)
    end

end
