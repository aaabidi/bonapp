class StatusesController < ApplicationController
  def create
    @amenity = Amenity.find(params[:amenity_id])

    @status = @amenity.statuses.create(statuses_params)

    redirect_to amenity_path(@amenity)
  end

  def index
    @status = Status.all.order("created_at DESC")
    @status = Status.new
  end

  private
    def statuses_params
      params.require(:status).permit(:reviewer, :status)
    end

end
