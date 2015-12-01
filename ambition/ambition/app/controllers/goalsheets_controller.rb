class GoalsheetsController < ApplicationController
  before_action :set_goalsheet, only: [:show, :edit, :update, :destroy]

  # GET /goalsheets
  # GET /goalsheets.json
  def index
    @goalsheets = Goalsheet.all
  end

  # GET /goalsheets/1
  # GET /goalsheets/1.json
  def show
  end

  # GET /goalsheets/new
  def new
    @goalsheet = Goalsheet.new
    3.times do
      task = @goalsheet.tasks.build
    end
  end

  # GET /goalsheets/1/edit
  def edit
  end

  # POST /goalsheets
  # POST /goalsheets.json
  def create
    @goalsheet = Goalsheet.new(goalsheet_params)
    respond_to do |format|
      if @goalsheet.save
        format.html { redirect_to @goalsheet, notice: 'Goalsheet was successfully created.' }
        format.json { render :show, status: :created, location: @goalsheet }
      else
        format.html { render :new }
        format.json { render json: @goalsheet.errors, status: :unprocessable_entity }
      end
    end
  end

  # PATCH/PUT /goalsheets/1
  # PATCH/PUT /goalsheets/1.json
  def update
    respond_to do |format|
      if @goalsheet.update(goalsheet_params)
        format.html { redirect_to @goalsheet, notice: 'Goalsheet was successfully updated.' }
        format.json { render :show, status: :ok, location: @goalsheet }
      else
        format.html { render :edit }
        format.json { render json: @goalsheet.errors, status: :unprocessable_entity }
      end
    end
  end

  # DELETE /goalsheets/1
  # DELETE /goalsheets/1.json
  def destroy
    @goalsheet.destroy
    respond_to do |format|
      format.html { redirect_to goalsheets_url, notice: 'Goalsheet was successfully destroyed.' }
      format.json { head :no_content }
    end
  end

  private
    # Use callbacks to share common setup or constraints between actions.
    def set_goalsheet
      @goalsheet = Goalsheet.find(params[:id])
    end

    # Never trust parameters from the scary internet, only allow the white list through.
    def goalsheet_params
      params.require(:goalsheet).permit(:time, :goals, tasks_attributes: [ :status, :description, :comments, :_destroy, :id ])
    end
end
